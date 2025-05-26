def ordenar_cinco_numeros():
    numeros = []
    for i in range(5):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    numeros.sort(reverse=True)
    print("Ordenados de mayor a menor:", numeros)

ordenar_cinco_numeros()