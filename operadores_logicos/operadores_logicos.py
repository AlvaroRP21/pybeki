# Ejercicio 1: Uso de and

edad = 25
tiene_identificacion = True

# Solo puede entrar si tiene más de 18 años y tiene identificación
if edad > 18 and tiene_identificacion:
    print("Puede entrar")
else:
    print("No puede entrar")



# Ejercicio propuesto: Declara dos variables: mayor_de_edad = True y tiene_ticket = False. Escribe una condición que imprima "Puede ingresar" solo si ambas condiciones son verdaderas.




# Ejercicio 2: Uso de or

dia = "sábado"

# Se descansa si es sábado o domingo
if dia == "sábado" or dia == "domingo":
    print("Es día de descanso")
else:
    print("Es día laboral")



# Ejercicio propuesto: Declara una variable clima = "lluvia". Escribe un programa que diga "Lleva paraguas" si el clima es "lluvia" o "nieve".


# Ejercicio 3: Uso de not
activo = False

# Solo mostramos mensaje si NO está activo
if not activo:
    print("El usuario está inactivo")


# Ejercicio propuesto: Declara la variable conectado = False. Escribe una condición que imprima "Usuario desconectado" si conectado es falso.


# Ejercicio 4: Combinación de and y or
edad = 17
con_permiso = True

# Puede entrar si es mayor de edad o si tiene permiso
if edad >= 18 or con_permiso:
    print("Puede entrar")
else:
    print("No puede entrar")


# Ejercicio propuesto: Crea dos variables: nota = 6 y examen_extra = True. El alumno aprueba si tiene nota mayor o igual a 7 o si hizo el examen extra.



# Ejercicio 5: Expresión lógica más compleja

edad = 20
estudiante = True

# Se aplica descuento si es menor de 18 o si es estudiante y menor de 25
if edad < 18 or (estudiante and edad < 25):
    print("Descuento aplicado")
else:
    print("No tiene descuento")

# Ejercicio propuesto: Crea las variables: cliente_frecuente = True, compra_mayor_a_100 = False. 
# El usuario obtiene un cupón si es cliente frecuente y su compra fue mayor a 100, o si es un nuevo cliente (nuevo_cliente = True).