# Ejercicio 1: Contador simple con while
# Ejercicio propuesto: Usa un bucle while para imprimir los números del 1 al 3.
print("\nEjercicio 1")

contador = 1

while contador <= 3:
    print("Numero:", contador)
    contador += 1


# Ejercicio 2: Contador hacia atrás
# Ejercicio propuesto: Escribe un programa que imprima los números del 3 al 1 usando un bucle while.
print("\nEjercicio 2")

contador = 3

while contador > 0:
    print(contador)
    contador -=1

# Ejercicio 3: Pedir datos hasta condición
# Ejercicio propuesto: Escribe un programa que pregunte al usuario una contraseña hasta que escriba "python123".
print("\nEjercicio 3")

palabra = ""

while palabra != "python123":
    palabra = input("Escribe una contraseña: ")


# Ejercicio 4: Acumulador con while
# Ejercicio propuesto: Suma los números del 1 al 4 usando un bucle while.
print("\nEjercicio 4")

suma = 0
numero = 1

while numero <= 4:
    suma += numero
    numero += 1

print("La suma total es:", suma)


# Ejercicio 5: Validar entrada del usuario
# Ejercicio propuesto: Escribe un programa que pida al usuario escribir "ok" y no termine hasta que lo haga.
print("\nEjercicio 5")

respuesta = ""

while respuesta != "ok":
    respuesta = input("¿Quieres continuar? (Escribe 'ok' para seguir): ")
print("\n")


