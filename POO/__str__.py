# Describe class
class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    def __str__(self):
        return self.name + ' is a ' + self.specie

cat = Animal("Itachi", "Cat")
print(cat)