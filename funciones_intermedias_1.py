# Funciones Intermedias - Ejercicios Core

print("=== 1. Actualizar valores en diccionarios y listas ===\n")

# 1.1 Cambiar el valor de 3 en matriz por 6
matriz = [[10, 15, 20], [3, 7, 14]]
print("Matriz original:", matriz)
matriz[1][0] = 6  # La fila 1 (índice 1), columna 0 (primer elemento)
print("Matriz modificada:", matriz)
print("¿Es correcto?", matriz == [[10, 15, 20], [6, 7, 14]])
print()

# 1.2 Cambiar el nombre del primer cantante
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
print("Cantantes original:", cantantes[0]["nombre"])
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes modificado:", cantantes[0]["nombre"])
print()

# 1.3 Cambiar "Cancún" por "Monterrey"
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
print("Ciudades de México original:", ciudades["México"])
ciudades["México"][2] = "Monterrey"  # índice 2 es la tercera posición
print("Ciudades de México modificado:", ciudades["México"])
print()

# 1.4 Cambiar el valor de "latitud"
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
print("Coordenadas original:", coordenadas[0]["latitud"])
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas modificado:", coordenadas[0]["latitud"])
print("\n" + "="*50 + "\n")

# 2. Función iterarDiccionario(lista)
print("=== 2. iterarDiccionario(lista) ===\n")

def iterarDiccionario(lista):
    for diccionario in lista:
        # Opción básica: cada llave y valor en líneas separadas
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
        print()  # línea en blanco entre diccionarios

# Bonus: Formato más limpio
def iterarDiccionarioBonus(lista):
    for diccionario in lista:
        items = []
        for llave, valor in diccionario.items():
            items.append(f"{llave} - {valor}")
        print(", ".join(items))

# Prueba con cantantes
cantantes_ejemplo = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("Formato básico (llave: valor en líneas separadas):")
iterarDiccionario(cantantes_ejemplo)

print("Formato bonus (nombre - valor, nombre - valor):")
iterarDiccionarioBonus(cantantes_ejemplo)
print("\n" + "="*50 + "\n")

# 3. Función iterarDiccionario2(llave, lista)
print("=== 3. iterarDiccionario2(llave, lista) ===\n")

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

print("Valores de 'nombre':")
iterarDiccionario2("nombre", cantantes_ejemplo)

print("\nValores de 'pais':")
iterarDiccionario2("pais", cantantes_ejemplo)
print("\n" + "="*50 + "\n")

# 4. Función imprimirInformacion(diccionario)
print("=== 4. imprimirInformacion(diccionario) ===\n")

def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        # Imprimir el nombre de la clave en mayúsculas con el tamaño de la lista
        print(f"{len(valores)} {clave.upper()}")
        # Imprimir cada valor de la lista
        for valor in valores:
            print(valor)
        print()  # línea en blanco entre cada clave

# Prueba con costa_rica
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)

