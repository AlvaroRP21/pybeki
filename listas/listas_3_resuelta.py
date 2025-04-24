# Ejercicio 1: Acceder a elementos en listas anidadas
# Ejercicio propuesto: Crea una lista con tres productos, donde cada producto tenga nombre y precio. Muestra el precio del tercer producto.
print("\nEjercicio 1")

productos = [["Doritos", 1.5], ["Botella de agua", 0.8], ["Mentos", 2]]
print(productos[2])


# Ejercicio 2: Recorrer listas anidadas con un bucle
# Ejercicio propuesto: Crea una lista de tres animales donde cada sublista contenga el nombre del animal y su tipo ("mamífero", "ave", etc.).
# Usa un bucle para imprimir frases como: "El perro es un mamífero."
print("\nEjercicio 2")

animales = [["Gato", "Mamifero"], ["Cocodrilo", "Reptil"], ["Halcon", "Ave"]]
for animal in animales:
    print("El", animal[0], "es un", animal[1])


# Ejercicio 3: Condicionales con listas anidadas
# Ejercicio propuesto: Crea una lista de empleados con su nombre y salario. Muestra solo los empleados que ganan más de 1000.
print("\nEjercicio 3")

empleados = [["Daniel", 1800], ["Ismael", 2400], ["Alvaro", 950], ["Jesus", 860], ["Miguel", 1200]]
# Dependiendo de lo que pongamos de sueldo, si es mayor que 1000 aparecera por pantalla
for empleado in empleados:
    if empleado[1] > 1000:
        print(empleado[0], "cobra", empleado[1])
    
print("")
