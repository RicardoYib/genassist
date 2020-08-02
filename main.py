import sys
import logging
from genassist.plant import GenericPlant, CloneStack
from genassist.genetics import GeneticPool

logger = logging.getLogger()



def main():
    
	logger.debug("Initializing Genetics Assistant...")
    
	hemp = GenericPlant(species='hemp', genes='YYGGGG')
	clones = CloneStack(species='hemp', genes='YYGGGG', navail=3)
	print clones.navail
	clones.subtract(2)
	print clones.genes
	
	gpool = GeneticPool("hemp")
	gpool.add_clones(genes="YYYWXH", navail=4)
	print gpool._get_genes_list()

if __name__ == '__main__':
    
    main()



