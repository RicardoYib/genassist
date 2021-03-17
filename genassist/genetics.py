import numpy     as np
import itertools 
from genassist.plant import CloneStack

genes_parameters = {
	'G': {
		"w":0.60,
		"score": 3.1},
	'Y': {
		"w":0.60,
		"score": 2},
	'H': {
		"w":0.60,
		"score": 1},
	'X': {
		"w":1.00,
		"score": -2},
	'W': {
		"w":1.00,
		"score": -2}
}
 

class GeneticPool ():
	
	def __init__ (self, species=None, best_gene=None):
		self.mvp = None
		self.best_crossbreeds = None # list of dicts with descending score order
		self.best_5050        = None # list of dicts with descending score order
		self._kinds = ['hemp']
		self.pool = []

		assert species is not None, ValueError("species must be specified")
		assert species.lower() in self._kinds, ValueError("'species' must be one of: {self._kinds}")
		if best_gene is not None: 
			assert best_gene in genes_parameters.keys(), ValueError("Invalid best gene <{best_gene}>")
		
		self.species = species.lower()
		self.best_gene = "G" if best_gene is None else best_gene
	
	def __str__(self):
		rtn = f"SPECIES:\t{self.species}\nAvailable clones: ({len(self.pool)})\n"

		for clones in self.pool:
			rtn += f"\t{clones}" + (" [MVP]" if clones == self.mvp else "") + "\n"
		return rtn
		
	def get_genes_list(self):
		return [cs.genes for cs in self.pool]
		
	def _refresh_mvp(self):
		mvp = None
		for clone_stack in self.pool:
			score = get_score(clone_stack, self.best_gene)
			if mvp is None:
				mvp = clone_stack
				continue
			mvp_score = get_score(mvp, self.best_gene)
			if score > mvp_score:
				mvp = clone_stack

		self.mvp = mvp
		
	def add_clones(self, genes=None, navail=None, parse_clone=None):
		assert genes not in self.get_genes_list(), ValueError("genes '{}' are already present in the genetics pool. use subtract() add() instead")
		if isinstance(parse_clone, CloneStack):
			self.pool.append(parse_clone)
		else:
			self.pool.append(CloneStack(navail=navail, species=self.species, genes=genes))

		self._refresh_mvp()
		self._compute_best_crossbreed()
		self._compute_5050()
	
	def _compute_crossbreed(self, clone_genes, total_clones):
		
		combinations = itertools.combinations(clone_genes, total_clones)
		all_scores = {}
		for comb in combinations:
			comb_winner_genes = ""
			# if there is some randomness in genetics, skip combination
			is_5050    = False
			is_lowprob = False
			many_5050  = False
			for slot in range(0, 6):
				breed_genes = "".join([g[slot] for g in comb])
				slot_scores = get_slot_scores(breed_genes)
				slot_winner_gene = max(slot_scores, key=slot_scores.get)
				winners = [k for k, v in slot_scores.items() if v == max(slot_scores.values())]
				if len(winners) == 2:
					# check if there was already a 5050 chance in previous slots
					if is_5050:
						many_5050 = True
					is_5050 = True
					# Set final genes with the best 5050 gene
					slot_winner_gene = winners[0]
					if genes_parameters[winners[1]]["score"] > genes_parameters[winners[0]]["score"]:
						slot_winner_gene = winners[1]
				elif len(winners) > 2:
					is_lowprob = True
				comb_winner_genes += slot_winner_gene
			if is_lowprob:
				final_score = 0
			else:
				final_score = get_score(comb_winner_genes, best_gene=self.best_gene)
			all_scores[comb_winner_genes] = {
				"score": final_score,
				"comb" : comb,
				"warning_5050": is_5050,
				"warning_many5050": many_5050
			}

			return all_scores
		
	def _compute_5050(self):
		if not self.best_crossbreeds:
			return
		winner = next(iter( self.best_crossbreeds.items() ))
		winner_gene  = winner[0]
		winner_score = winner[1]["score"]

		# Check that clone base has all 6 greens
		has_red = True if len([g for g in winner_gene if genes_parameters[g]["score"] < 0]) > 0 else False
		if has_red: return
		# add two copies of the best 6 green clone
		clone_base = [winner_gene, winner_gene]

		aux_clone_combinations = itertools.combinations(self.get_genes_list(), 2)

		all_scores = {}
		for aux_clone_1, aux_clone_2 in aux_clone_combinations:
			clone_genes = clone_base + [aux_clone_1] + [aux_clone_2]
			all_scores.update(self._compute_crossbreed(clone_genes, 4))

		
		best_5050 = {k: v for k, v in sorted(all_scores.items(), key=lambda item: item[1]["score"], reverse=True)}
		print(best_5050)
		if best_5050 and next(iter( best_5050.items() ))[1]["score"] > winner_score:
			self.best_5050 = best_5050
	
	def _compute_best_crossbreed(self):
		clone_genes = self.get_genes_list()
		# print(clone_genes)

		# get number of possible clone candidates total count
		n_clone_options = range(3, len(clone_genes)+1)
		all_scores = {}
		for total_clones in n_clone_options:
			all_scores.update(self._compute_crossbreed(clone_genes, total_clones))

		# Add single genes in case they are better
		for clone in clone_genes:
			score = get_score(clone, best_gene=self.best_gene)
			if clone not in all_scores.keys() or ( clone in all_scores.keys() and score >= all_scores[clone]["score"] ):
				all_scores[clone] = {
					"score": score,
					"comb" : None,
					"warning_5050": False,
					"warning_many5050": False
				}

		self.best_crossbreeds = {k: v for k, v in sorted(all_scores.items(), key=lambda item: item[1]["score"], reverse=True)}
		# print(all_scores)
		# print({k: v for k, v in sorted(all_scores.items(), key=lambda item: item[1]["score"], reverse=True)})
		
		
def get_score(clone, best_gene):
	score = 0
	n_g   = 0
	n_y   = 0
	genes = clone.genes if isinstance(clone, CloneStack) else clone
	for g in genes:
		if   g.upper() == "Y": n_y += 1
		elif g.upper() == "G": n_g += 1
		score += genes_parameters[g.upper()]["score"]

	# Improve score of perfect clone
	if best_gene == "G":
		if   n_g == 4 and n_y == 2: score += 200 
		elif n_g == 5 and n_y == 1: score += 100 
	elif best_gene == "Y":
		if   n_y == 4 and n_g == 2: score += 200 
		elif n_y == 5 and n_g == 1: score += 100 

	return score

def get_slot_scores(breed_genes):
    gene_types = genes_parameters.keys()
    scores = {gene_type: 0 for gene_type in gene_types}
    for gene in breed_genes:
        scores[gene] += genes_parameters[gene]["w"]

    return scores
