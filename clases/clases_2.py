# Ejercicio 1: Getter básico con @property

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre  # atributo privado

    @property
    def nombre(self):
        return self._nombre

p = Persona("Carlos")
print(p.nombre)  # Accede al getter


# Ejercicio propuesto: Crea una clase Animal con un atributo privado _especie y un método getter que devuelva ese valor. Crea un objeto y muestra la especie.







# Ejercicio 2: Setter para modificar un valor
class Producto:
    def __init__(self, precio):
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio

p = Producto(100)
p.precio = 120  # Usa el setter
print(p.precio)



# Ejercicio propuesto: Crea una clase Libro con un atributo _titulo, un getter y un setter para modificarlo. Crea un objeto, cambia el título y muéstralo.






# Ejercicio 3: Validar datos en el setter
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, cantidad):
        if cantidad >= 0:
            self._saldo = cantidad
        else:
            print("El saldo no puede ser negativo")

c = CuentaBancaria(500)
c.saldo = -100  # No se actualiza
print(c.saldo)  # Imprime 500


# Ejercicio propuesto: Crea una clase Estudiante con un atributo nota que solo permita valores entre 0 y 10. Si no, muestra un mensaje de error.