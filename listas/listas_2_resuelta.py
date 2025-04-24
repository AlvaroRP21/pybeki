# Ejercicio 1: Verificar si un elemento está en la lista
# Ejercicio propuesto: Crea una lista con tres nombres. Pregunta si el nombre "Ana" está en la lista y muestra un mensaje dependiendo del resultado.
print("\nEjercicio 1")

nombres = ["Wenceslao", "Natalia", "Pablo"]
# Si añadimos a Ana a la lista escribira "Ana esta en la lista"
# En el caso en el que no se encuentre "Ana" en la lista excribira "Ana no esta en la lista"

if "Ana" in nombres:
    print("Ana esta en la lista")
else:
    print("Ana no esta en la lista")


# Ejercicio 2: Contar cuántos elementos cumplen una condición
# Ejercicio propuesto: Crea una lista de edades y cuenta cuántas personas son mayores o iguales a 18 años.
print("\nEjercicio 2")

edades = [17, 24, 8, 67, 33]
# Al poner numeros mayores o igual a 18, en el for se añadira + 1 a el contador
contador = 0

for edad in edades:
    if edad >= 18:
        contador += 1

print("Hay", contador, "mayores de edad")


# Ejercicio 3: Buscar el valor máximo si cumple una condición
# Ejercicio propuesto: Dada una lista de temperaturas, encuentra la mayor temperatura que sea menor a 40 grados.
print("\nEjercicio 3")

temperaturas = [-2, 13, 24, 1]
# Dependiendo de los numeros que pongamos, cogera el que tiene un valor mas alto
# Aparte de que debe de ser menor a 40
mayor = 0

for temperatura in temperaturas:
    if temperatura < 40 and temperatura > mayor:
        mayor = temperatura

print("La mayor temperatura menor a 40 es:", mayor, "\n")
