#Explicar un programa que permita calcular el área de diferentes figuras geométricas
# utilizando el concepto de herencia en programación orientada a objetos.
class ClaseBase:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

    def __str__(self):
        return self.nombre

class Rectangulo(ClaseBase):
    def __init__(self, largo, ancho):
        super().__init__("Rectángulo")
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class Triangulo(ClaseBase):
    def __init__(self, altura, base):
        super().__init__("Triángulo")
        self.altura = altura
        self.base = base

    def area(self):
        return (self.base * self.altura) / 2

# Creación de objetos y cálculos
a = Rectangulo(80, 70)
b = Triangulo(66, 54)

print("La figura es:", b)
print("El área de la figura es:", b.area())
print("La figura es:", a)
print("El área de la figura es:", a.area())
