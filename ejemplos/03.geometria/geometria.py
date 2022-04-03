class Figura:
    pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

# TODO: Pensar en otra posible herencia (taxonomía)

# Pruebas
c1 = Cuadrado(6)
c2 = Cuadrado(4)
print(c1.perimetro())
print(c2.perimetro())

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print(r1.perimetro())
print(r2.perimetro())