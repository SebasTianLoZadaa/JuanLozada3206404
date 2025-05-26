def suma_hasta_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

entrada = input("Ingrese un número: ")

if entrada.isdigit():
    n = int(entrada)
    if n > 1:
        print("La suma es:", suma_hasta_n(n))
    else:
        print("Ingrese un número entero valido")
else:
    print("Ingrese un valor NUMERICO")
