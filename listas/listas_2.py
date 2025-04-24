# Ejercicio 1: Verificar si un elemento está en la lista

colores = ["rojo", "azul", "verde"]

# Verificamos si "azul" está en la lista
if "azul" in colores:
    print("¡Azul está en la lista!")
else:
    print("Azul no está en la lista.")


# Ejercicio propuesto: Crea una lista con tres nombres. Pregunta si el nombre "Ana" está en la lista y muestra un mensaje dependiendo del resultado.





# Ejercicio 2: Contar cuántos elementos cumplen una condición
numeros = [5, 12, 7, 20, 3]
contador = 0

# Contamos cuántos números son mayores que 10
for numero in numeros:
    if numero > 10:
        contador += 1

print("Hay", contador, "números mayores que 10.")


# Ejercicio propuesto: Crea una lista de edades y cuenta cuántas personas son mayores o iguales a 18 años.



# Ejercicio 3: Buscar el valor máximo si cumple una condición
precios = [100, 250, 80, 300]
maximo = 0

# Encontramos el mayor precio que sea menor a 300
for precio in precios:
    if precio < 300 and precio > maximo:
        maximo = precio

print("El mayor precio menor a 300 es:", maximo)

# Ejercicio propuesto: Dada una lista de temperaturas, encuentra la mayor temperatura que sea menor a 40 grados.