# Ejercicio 1: Crear y acceder a un diccionario
persona = {
    "nombre": "Ana",
    "edad": 30
}

print(persona["nombre"])  # Imprime "Ana"


# Ejercicio propuesto: Crea un diccionario llamado coche con las claves marca y año. Muestra el valor de marca.






# Ejercicio 2: Agregar un nuevo par clave-valor
usuario = {"nombre": "Carlos"}
usuario["edad"] = 25
print(usuario)  # Imprime {'nombre': 'Carlos', 'edad': 25}


# Ejercicio propuesto: Crea un diccionario con la clave animal = "perro", y luego agrega una nueva clave color = "marrón".






# Ejercicio 3: Recorrer un diccionario con un bucle
frutas = {
    "manzana": 3,
    "banana": 5,
    "pera": 2
}

for fruta in frutas:
    print(fruta, ":", frutas[fruta])


# Ejercicio propuesto: Crea un diccionario con tres países y su capital. Recorre el diccionario e imprime cada país con su capital.









# Ejercicio 4: Usar condicionales con diccionarios

productos = {"pan": 1.5, "leche": 0.9}

if "leche" in productos:
    print("Sí hay leche.")
else:
    print("No hay leche.")


# Ejercicio propuesto: Crea un diccionario inventario con lápiz y cuaderno. Verifica si hay borrador en el inventario.




# Ejercicio 5: Eliminar un elemento del diccionario
colores = {"rojo": "#FF0000", "azul": "#0000FF"}
del colores["rojo"]
print(colores)  # Solo queda azul


# Ejercicio propuesto: Crea un diccionario alumno = {"nombre": "Luis", "edad": 20, "grado": "10°"} y elimina la clave grado.