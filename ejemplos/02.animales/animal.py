# Pilares del POO

class Animal:
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