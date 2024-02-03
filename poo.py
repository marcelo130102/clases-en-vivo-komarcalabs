# Programación Orientada a Objetos


class Coche:
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(
            f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.enMarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}"
        )

#this -> self

# coche1 = Coche()
# print(coche1.estado())
# coche1.arrancar()
# print(coche1.estado())

# Usando el constructor

# vehiculo1 = Vehiculo("Mazda", "MX5")

# print(vehiculo1.estado())


# funcion (var1_in, var2_in, var3_in)
# atributos: var1, var2, var3

# Herencia

class Padre:
    def __init__(self):
        print("Soy el padre")

    def metodo_padre(self):
        print("Este es el método padre")


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        print("Soy el hijo")

    def metodo_hijo(self):
        print("Este es el método hijo")


hijo1 = Hijo()
hijo1.metodo_padre()
hijo1.metodo_hijo()