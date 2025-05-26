def suma_pares_entre(a, b):
    suma = 0
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            suma += i
    return suma

def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            n = int(entrada)
            if n >= 0:
                return n
            else:
                print("El número debe ser positivo o cero.")
        else:
            print("Entrada inválida, por favor ingrese un número entero positivo.")
            
a = pedir_numero("Ingrese el primer número: ")
b = pedir_numero("Ingrese el segundo número: ")

resultado = suma_pares_entre(a, b)
print("La suma de pares entre", a, "y", b, "es:", resultado)
