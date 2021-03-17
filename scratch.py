import numpy     as np
import itertools 

from genassist.genetics import get_score

def get_slot_scores(breed_genes):
    gene_types = genes_parameters.keys()
    scores = {gene_type: 0 for gene_type in gene_types}
    for gene in breed_genes:
        scores[gene] += genes_parameters[gene]["w"]

    return scores

genes_parameters = {
	'G': {
		"w":0.60,
		"score": 3},
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
best_clone = "G"
clone_genes = ["HGHHHG", "GGGYHH", "GGHGYH", "GGHGHG", "YYYYYG", "YGGYHH"]

# get number of possible clone candidates total count
n_clone_options = range(3, len(clone_genes)+1)

all_scores = {}

for total_clones in n_clone_options:
    combinations = itertools.combinations(clone_genes, total_clones)
    for comb in combinations:
        comb_score = 0
        comb_winner_genes = ""
        # if there is some randomness in genetics, skip combination
        is_5050    = False
        is_lowprob = False
        many_5050  = False
        for slot in range(0, 6):
            breed_genes = "".join([g[slot] for g in comb])
            slot_scores = get_slot_scores(breed_genes)
            final_slot_score = genes_parameters[max(slot_scores, key=slot_scores.get)]["score"]
            slot_winner_gene = max(slot_scores, key=slot_scores.get)
            winners = [k for k, v in slot_scores.items() if v == max(slot_scores.values())]
            if len(winners) == 2:
                # check if there was already a 5050 chance in previous slots
                if is_5050:
                    many_5050 = True
                # other_winner = [g for g in slot_scores.keys() if slot_scores[g] == max(slot_scores.values()) and g != slot_winner_gene][0]
                # final_slot_score = np.mean([genes_parameters[slot_winner_gene]["score"], genes_parameters[other_winner]["score"]])
                # slot_winner_gene = "[{}/{}]".format(slot_winner_gene, other_winner)
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
            final_score = get_score(comb_winner_genes, best_gene=best_clone)

        all_scores[comb_winner_genes] = {
            "score": final_score,
            "comb" : comb,
            "warning_5050": is_5050,
            "warning_many5050": many_5050
        }
        

# print(all_scores)
print({k: v for k, v in sorted(all_scores.items(), key=lambda item: item[1]["score"], reverse=True)})
