# Ejercicio 1: Crear y mostrar una lista
# Ejercicio propuesto: Crea una lista con tres nombres de tus amigos y muéstrala en pantalla.
print("\nEjercicio 1")

amigos = ["Nicolas", "Alejandro", "David"]
print(amigos)


# Ejercicio 2: Acceder a elementos de una lista
# Ejercicio propuesto: Crea una lista de tres animales y muestra el primero de la lista.
print("\nEjercicio 2")

animales = ["Perro", "Gato", "Caballo"]
print(animales[0])


# Ejercicio 3: Modificar un elemento de la lista
# Ejercicio propuesto: Crea una lista con tres ciudades y cambia la segunda ciudad por otra diferente. Luego imprime la lista.
print("\nEjercicio 3")

ciudades = ["Barcelona", "Chicago", "Nueva York"]
ciudades[1] = "Roma"
print(ciudades)


# Ejercicio 4: Agregar elementos a una lista
# Ejercicio propuesto: Crea una lista con dos deportes y agrega un tercer deporte al final. Imprime la lista actualizada.
print("\nEjercicio 4")

deportes = ["Futbol", "Baloncesto"]
deportes.append("Baseball")
print(deportes)


# Ejercicio 5: Recorrer una lista con un bucle
# Ejercicio propuesto: Crea una lista con tres comidas favoritas y utiliza un bucle for para imprimir cada una en una línea distinta.
print("\nEjercicio 5")

comidas = ["Burrito", "Pizza", "Hamburguesa\n"]
for comida in comidas:
    print(comida)


