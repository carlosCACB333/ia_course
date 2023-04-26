class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Creamos un rectángulo de base 4 y altura 3
mi_rectangulo = Rectangulo(4, 3)

# Calculamos el área del rectángulo
area_rectangulo = mi_rectangulo.area()
print("El área del rectángulo es:", area_rectangulo)

# Calculamos el perímetro del rectángulo
perimetro_rectangulo = mi_rectangulo.perimetro()
print("El perímetro del rectángulo es:", perimetro_rectangulo)
