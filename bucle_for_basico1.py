# 1. Básico: imprime todos los números enteros del 0 al 100
print("=== 1. Básico: 0 al 100 ===")
for i in range(0, 101):
    print(i)

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("\n=== 2. Múltiples de 2 (2 al 500) ===")
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice: del 1 al 100.
#    Si divisible por 5 imprime "ice ice"
#    Si divisible por 10 imprime "baby"
print("\n=== 3. Contando Vanilla Ice ===")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# 4. Wow. Número gigante a la vista:
#    suma los números pares del 0 al 500,000 e imprime la suma total
print("\n=== 4. Suma de pares del 0 al 500,000 ===")
suma_pares = 0
for i in range(0, 500001, 2):
    suma_pares += i
print(f"La suma total es: {suma_pares}")

# 5. Regrésame al 3:
#    imprime los números positivos desde 2024 en cuenta regresiva de 3 en 3
print("\n=== 5. Regresiva desde 2024 de 3 en 3 ===")
for i in range(2024, 0, -3):
    print(i)

# 6. Contador dinámico:
#    numInicial, numFinal, multiplo
#    Imprime los enteros entre numInicial y numFinal que sean múltiplos de multiplo
print("\n=== 6. Contador dinámico ===")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)