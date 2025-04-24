# Ejercicio 1: Acceder a elementos en listas anidadas
# Lista de estudiantes con su edad
estudiantes = [["Ana", 20], ["Luis", 22], ["María", 19]]

# Imprimimos el nombre del segundo estudiante
print(estudiantes[1][0])  # Imprime "Luis"


# Ejercicio propuesto: Crea una lista con tres productos, donde cada producto tenga nombre y precio. Muestra el precio del tercer producto.

# Ejercicio 2: Recorrer listas anidadas con un bucle

# Lista de personas con nombre y país
personas = [["Carlos", "México"], ["Sofía", "Argentina"], ["Miguel", "Perú"]]

# Imprimimos todos los nombres con sus países
for persona in personas:
    print(persona[0], "es de", persona[1])


# Ejercicio propuesto: Crea una lista de tres animales donde cada sublista contenga el nombre del animal y su tipo ("mamífero", "ave", etc.).
# Usa un bucle para imprimir frases como: "El perro es un mamífero."


# Ejercicio 3: Condicionales con listas anidadas
# Lista de alumnos con su calificación
alumnos = [["Pedro", 85], ["Lucía", 60], ["Andrés", 90]]

# Mostramos solo los que aprobaron (nota mayor o igual a 70)
for alumno in alumnos:
    if alumno[1] >= 70:
        print(alumno[0], "aprobó con", alumno[1])


# Ejercicio propuesto: Crea una lista de empleados con su nombre y salario. Muestra solo los empleados que ganan más de 1000.
