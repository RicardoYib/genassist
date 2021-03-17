import sys
import logging
from genassist.plant import GenericPlant, CloneStack
from genassist.genetics import GeneticPool

logger = logging.getLogger()



def main():
    
	logger.debug("Initializing Genetics Assistant...")
    
	clone_genes = ["HGHHHG", "GGGYHH", "GGHGYH", "GGHGHG", "YYYYYG", "YGGYHH"]
	clones = [CloneStack(species='hemp', genes=g, navail=3) for g in clone_genes]
	
	
	gpool = GeneticPool("hemp", best_gene="G")
	for clone in clones:
		gpool.add_clones(parse_clone=clone)

	print(gpool)
	print(gpool.best_crossbreeds)

if __name__ == '__main__':
    
    main()


# TODO: continuar con metodo 50/50
