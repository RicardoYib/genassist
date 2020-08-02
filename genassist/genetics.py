from plant import CloneStack

genes_weight = {
	'Y' = 0.6,
	'G' = 0.6, 
	'H' = 0.6, 
	'W' = 1.0, 
	'X' = 1.0
}
good_genes = ['Y', 'G', 'H']
bad_genes  = ['W', 'X']
 

class GeneticPool ():
	_kinds = ['hemp']
	pool = []
	
	def __init__ (self, species=None):
		assert species is not None, ValueError("species must be specified")
		assert species.lower() in self._kinds, ValueError("'species' must be one of: {self._kinds}".format(species))
		
		self.species = species.lower()
		# self.set_goal(goal) # currently not needed
		
	# def set_goal(self, goal):
		# assert all([g in ['Y', 'G', 'H', 'W', 'X'] for g in goal]), ValueError("Invalid goal genetics")
		# self.goal = goal
		
	def _get_genes_list(self):
		return [cs.genes for cs in self.pool]
		
	def _refresh_mvp(self):
		mvp = None
		for clone_stack in self.pool:
			score = get_genes_score(clone_stack.genes)
			if mvp is None:
				mvp = clone_stack
				continue
			mvp_score = get_genes_score(mvp.genes)
			if score > mvp_score:
				CONTINUE HERE
		
		
	def optimize_5050(self):
		pass
		
	def add_clones(self, genes=None, navail=None):
		assert genes not in self._get_genes_list(), ValueError("genes '{}' are already present in the genetics pool. use subtract() add() instead")
		self.pool.append(CloneStack(navail=navail, species=self.species, genes=genes))
		
		
def get_genes_score(genes):
	score = 0
	for g in genes:
		score += genes_weight[g.upper()]