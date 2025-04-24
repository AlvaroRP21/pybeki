# Crea la clase Contador, tendra una propiedad valor = 0
# Tendra un metodo llamado incrementar que sumara 1 a valor
# Tendra un metodo llamado decrementar que restara 1 a valor
# Tendra un metodo llamado mostrar que mostrara un mensaje de cuanto es nuestro valor
# Tendra un metodo llamado incrementar_aleatorio que sumara un numero aleatorio entre 1 y 6 a valor
from random import *


class Contador:

    valor: int

    def __init__(self, valor_de_inicio):
        self.valor = valor_de_inicio
        
    def mostrar(self) -> None:
        print(f"Mi contador vale: {self.valor}")

    def incrementar(self, incremento):
        self.valor += incremento

    def calculo(self, calc, simbolo):
        if simbolo == "+":
            self.valor += calc

        elif simbolo == "-":
            self.valor -= calc
        
        elif simbolo == "*":
            self.valor *= calc

        elif simbolo == "/":
            self.valor /= calc

    def incrementar_aleatorio(self):

        numero_aleatorio = (randint(1, 6))
        self.valor += numero_aleatorio


# mi_contador = Contador(valor_de_inicio=0)

# mi_contador.mostrar()

# mi_contador.incrementar_aleatorio()

# mi_contador.mostrar()

# mi_contador.incrementar_aleatorio()

# mi_contador.mostrar()

# Incrementar el valor
# mi_contador.incrementar(incremento=5)
# mi_contador.mostrar()
# mi_contador.incrementar(incremento=2)
# mi_contador.calculo(calc=2, simbolo= "*")
# mi_contador.mostrar()





















# mi_contador_2 = Contador(valor_de_inicio=10)
# c.incrementar = + 1
# c.decrementar = -1
# c.mostrar = 0
# c.incrementar_aleatorio = randint(1, 6)

# print()
# print(c.incrementar_aleatorio)
