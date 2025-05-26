def suma_hasta_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Ingrese un número N: "))
print("La suma es:", suma_hasta_n(n))