"""A module with talking animals."""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f'{self.name} says {self.sound()}')

    @abstractmethod
    def sound(self):
        pass

class Cow(Animal):
    def sound(self):
        return 'moo'

class Horse(Animal):
    def sound(self):
        return 'neigh'

class Sheep(Animal):
    def sound(self):
        return 'baaaaa'

if __name__ == '__main__':
    s = Horse('Art')
    s.speak()
    c = Cow('Frankie')
    c.speak()
    Sheep('Little Thing').speak()