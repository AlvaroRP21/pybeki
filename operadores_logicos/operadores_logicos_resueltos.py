# Ejercicio 1: Uso de and
# Ejercicio propuesto: Declara dos variables: mayor_de_edad = True y tiene_ticket = False. Escribe una condición que imprima "Puede ingresar" solo si ambas condiciones son verdaderas.
print("\nEjercicio 1")

mayor_de_edad = True
tiene_ticket = False 
#para poder ingresar hay que cambiar estas variables ambas a True

if mayor_de_edad and tiene_ticket:
    print("Puede ingresar")
else:
    print("No puede ingresar")


# Ejercicio 2: Uso de or
# Ejercicio propuesto: Declara una variable clima = "lluvia". Escribe un programa que diga "Lleva paraguas" si el clima es "lluvia" o "nieve".
print("\nEjercicio 2")

clima = "lluvia" 
#Al cambiar la variable clima a "lluvia" o "nieve" te escribira "Lleva paraguas"
#En cualquier otro caso te escribira "No lleves paraguas"

if clima == "lluvia" or clima == "nieve":
    print("LLeva paraguas")
elif clima == "Lluvia" or clima == "Nieve":
    print("LLeva paraguas")
else:
    print("No lleves paraguas")


# Ejercicio 3: Uso de not
# Ejercicio propuesto: Declara la variable conectado = False. Escribe una condición que imprima "Usuario desconectado" si conectado es falso.
print("\nEjercicio 3")

conectado = False
# Si la variable conectado es "False" escribira "Usuario desconectado"
# En el caso que lo cambiemos a "True" escribira "Usuario conectado"

if not conectado:
    print("Usuario desconectado")
else:
    print("Usuario conectado")


# Ejercicio 4: Combinación de and y or
# Ejercicio propuesto: Crea dos variables: nota = 6 y examen_extra = True. El alumno aprueba si tiene nota mayor o igual a 7 o si hizo el examen extra.
print("\nEjercicio 4")

nota = 6
examen_extra = True
# Mientras la variable "nota" sea igual o mayor que "7"
# O la variable "examen_extra" sea "True"
# El alumno estara aprobado

if nota >= 7 or examen_extra:
    print("Alumno aprobado")
else:
    print("Alumno suspenso")


# Ejercicio 5: Expresión lógica más compleja
# Ejercicio propuesto: Crea las variables: cliente_frecuente = True, compra_mayor_a_100 = False. 
# El usuario obtiene un cupón si es cliente frecuente y su compra fue mayor a 100, o si es un nuevo cliente (nuevo_cliente = True).
print("\nEjercicio 5")

cliente_frecuente = True
compra_mayor_a_100 = False
# Si estas dos variables son "True" obtienes un cupon
nuevo_cliente = False
# Si esta variable es "True" tambien obtienes un cupon

if nuevo_cliente == True or (cliente_frecuente and compra_mayor_a_100 == True):
    print("Obtiene un cupon\n")
else:
    print("No obtiene un cupon\n")


