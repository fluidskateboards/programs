class Cat:
    family = 'feline'
    def __init__(self, n):
        self.name = n
a = Cat("Arturo")
b = Cat("Mr. Whiskers")
print(a.name, b.name, a.family, b.family, Cat.family)
Cat.family = "Feline"
print(a.name, b.name, a.family, b.family, Cat.family)