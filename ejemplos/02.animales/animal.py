# Pilares del POO
# Abstraccion: el concepto que queda representado por las clases y los métodos
# Herencia: Dada por la relación de Perro es un Animal y Gato es un Animal
# Encapsulamiento: No es el mejor ejemplo  

class Animal:
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    __texto_hablar__ = 'Guau!'

    def hablar(self):
        print(self.__texto_hablar__)    

class Gato(Animal):
    def hablar(self):
        print('Miau!')   

for animal in Perro(), Gato():
    animal.hablar()

#print(Perro().texto_hablar)    