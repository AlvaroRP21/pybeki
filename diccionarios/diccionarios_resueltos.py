# Ejercicio 1: Crear y acceder a un diccionario
# Ejercicio propuesto: Crea un diccionario llamado coche con las claves marca y año. Muestra el valor de marca.
print("Ejercicio 1")

coche = {
    "marca": "Ford",
    "año": 2015
}

print(coche["marca"])


# Ejercicio 2: Agregar un nuevo par clave-valor
# Ejercicio propuesto: Crea un diccionario con la clave animal = "perro", y luego agrega una nueva clave color = "marrón".
print("\nEjercicio 2")

animal = {"perro": "Pastor aleman"}
animal["color"] = "marron"
print(animal)


# Ejercicio 3: Recorrer un diccionario con un bucle
# Ejercicio propuesto: Crea un diccionario con tres países y su capital. Recorre el diccionario e imprime cada país con su capital.
print("\nEjercicio 3")

paises = {
    "Alemania": "Berlin",
    "Francia": "Paris",
    "Grecia": "Atenas"
}

for pais in paises:
    print(pais, ":", paises[pais])


# Ejercicio 4: Usar condicionales con diccionarios
# Ejercicio propuesto: Crea un diccionario inventario con lápiz y cuaderno. Verifica si hay borrador en el inventario.
print("\nEjercicios 4")

inventario = {"Lapiz", "Cuarderno"}
# Dependera si añadimos o quitamos "Borrador" a inventario, escribira una cosa u otra

if "Borrador" in inventario:
    print("Si hay borradores")
else:
    print("No hay borradores")


# Ejercicio 5: Eliminar un elemento del diccionario
# Ejercicio propuesto: Crea un diccionario alumno = {"nombre": "Luis", "edad": 20, "grado": "10°"} y elimina la clave grado.
print("\nEjercicio 5")

alumno = {"nombre": "Luis", "edad": 20, "grado": "10°"}
del alumno["grado"]
print(alumno)
print("")
