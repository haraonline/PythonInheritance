class Animal:
    def __init__(self, name, species):
        self.name = name
        self._species = species

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if value.lower() not in ['cat', 'feline']:
            raise ValueError('Species must be cat or feline')
        self._species = value

    # @species.deleter
    # def species(self):
    #     del self._species


cat = Animal('Kitty', 'Cat')
print(cat.name)
print(cat.species)

cat.species = 'Feline'
print(cat.species)