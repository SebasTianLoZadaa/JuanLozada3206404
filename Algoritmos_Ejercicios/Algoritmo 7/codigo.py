import random

def contar_apariciones():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("Lista:", lista)
    objetivo = int(input("Ingrese el número a buscar: "))
    cantidad = lista.count(objetivo)
    if cantidad > 0:
        print(f"El número {objetivo} aparece {cantidad} veces.")
    else:
        print("Número no encontrado")

contar_apariciones()