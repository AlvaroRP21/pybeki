# Ejercicio 1: Getter básico con @property
# Ejercicio propuesto: Crea una clase Animal con un atributo privado _especie y un método getter que devuelva ese valor. Crea un objeto y muestra la especie.
print("\nEjercicio 1")

class Animal:
    def __init__(self, especie):
        self._especie = especie

    @property
    def especie(self):
        return self._especie
    
e = Animal("Mamifero")
print(e.especie)


# Ejercicio 2: Setter para modificar un valor
# Ejercicio propuesto: Crea una clase Libro con un atributo _titulo, un getter y un setter para modificarlo. Crea un objeto, cambia el título y muéstralo.
print("\nEjercicio 2")

class Libro:
    def __init__(self, titulo):
        self._titulo = titulo

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

t = Libro("Quijote")
t.titulo = "El Quijote"
print(t.titulo)


# Ejercicio 3: Validar datos en el setter
# Ejercicio propuesto: Crea una clase Estudiante con un atributo nota que solo permita valores entre 0 y 10. Si no, muestra un mensaje de error.
print("\nEjercicio 3")

class Estudiante:
    def __init__(self, nota):
        self._nota = nota

    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, calificacion):
        if calificacion >= 0 and calificacion <= 10:
            self._nota = calificacion
        else:
            print("La calificacion debe de ser entre 0 y 10")

e = Estudiante(0)
e.nota = 5
print(e.nota, "\n")

