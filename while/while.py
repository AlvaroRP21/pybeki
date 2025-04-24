# Ejercicio 1: Contador simple con while
contador = 1

while contador <= 5:
    print("Número:", contador)
    contador += 1

# Ejercicio propuesto: Usa un bucle while para imprimir los números del 1 al 3.





# Ejercicio 2: Contador hacia atrás
contador = 5

while contador > 0:
    print(contador)
    contador -= 1


# Ejercicio propuesto: Escribe un programa que imprima los números del 3 al 1 usando un bucle while.



# Ejercicio 3: Pedir datos hasta condición

palabra = ""

while palabra != "salir":
    palabra = input("Escribe una palabra (o 'salir' para terminar): ")


# Ejercicio propuesto: Escribe un programa que pregunte al usuario una contraseña hasta que escriba "python123".





# Ejercicio 4: Acumulador con while
suma = 0
numero = 1

while numero <= 5:
    suma += numero
    numero += 1

print("La suma total es:", suma)

# Ejercicio propuesto: Suma los números del 1 al 4 usando un bucle while.






# Ejercicio 5: Validar entrada del usuario
respuesta = ""

while respuesta != "sí":
    respuesta = input("¿Quieres continuar? (escribe 'sí' para seguir): ")




# Ejercicio propuesto: Escribe un programa que pida al usuario escribir "ok" y no termine hasta que lo haga.