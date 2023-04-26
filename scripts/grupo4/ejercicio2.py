class Dispositivo:
    def __init__(self, precio, stock):
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Precio: {self.precio}, Stock: {self.stock}"


class Telefono(Dispositivo):
    def __init__(self, precio, stock, ram, pantalla):
        super().__init__(precio, stock)
        self.ram = ram
        self.pantalla = pantalla

    def __str__(self):
        return f"Telefono: {super().__str__()}, RAM: {self.ram}, Pantalla: {self.pantalla}"


class Laptop(Dispositivo):
    def __init__(self, precio, stock, ram, pantalla):
        super().__init__(precio, stock)
        self.ram = ram
        self.pantalla = pantalla

    def __str__(self):
        return f"Laptop: {super().__str__()}, RAM: {self.ram}, Pantalla: {self.pantalla}"


class Tablet(Dispositivo):
    def __init__(self, precio, stock, almacenamiento, resolucion):
        super().__init__(precio, stock)
        self.almacenamiento = almacenamiento
        self.resolucion = resolucion

    def __str__(self):
        return f"Tablet: {super().__str__()}, Almacenamiento: {self.almacenamiento}, Resolucion: {self.resolucion}"


#Ingreso de datos
telefono1 = Telefono(250, 2, 4, 5.5)
laptop1 = Laptop(1500, 1, 8, 15.5)
tablet1 = Tablet(250, 2, 64, "1920x1200")

print(telefono1)
print(laptop1)
print(tablet1)
