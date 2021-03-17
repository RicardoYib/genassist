import sys


class GenericPlant ():
	_kinds = ['hemp']
	
	def __init__ (self, species=None, genes=None, is_random=None):
		assert species is not None, ValueError("species must be specified")
		assert species.lower() in self._kinds, ValueError("'species' must be one of: {self._kinds}".format(species))
		assert isinstance(genes, str), ValueError("'genetics' must be a 6 character string: {}".format(genes))
		assert len(genes) == 6, ValueError("'genetics' must be a 6 character string: {}".format(genes))
		assert all([g in ['Y', 'G', 'H', 'W', 'X'] for g in genes]), ValueError("Invalid genetics")
		
		self.species = species.lower()
		self.genes = genes
		self.is_random = is_random if is_random is not None else False


class CloneStack (GenericPlant):
	
	
	def __init__ (self, navail=None, **kwargs):
	
		assert isinstance(navail, int), ValueError("'navail' must be an int")
		
		self.navail = navail
		
		GenericPlant.__init__(self, **kwargs)
		
	def subtract(self, s=1):
		self.navail -= s
		
	def add(self, a=1):
		self.navail += a

	def __str__(self):
		return "[{}]x{}".format(self.genes, self.navail)