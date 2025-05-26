def aparece_mas_veces_que_el_mayor(lista, numero):
    return lista.count(numero) > lista.count(max(lista))

def media_total(lista):
    return sum(lista) / len(lista)

def media_mayor_menor(lista):
    return (max(lista) + min(lista)) / 2

def lista_invertida(lista):
    return lista[::-1]

def menu():
    lista = [3, 7, 3, 2, 9, 3, 5, 9]

    while True:
        print("\nMenú de opciones:")
        print("1. Ver lista")
        print("2. Verificar si un número aparece más veces que el mayor")
        print("3. Calcular la media de todos los números")
        print("4. Calcular la media entre el mayor y el menor")
        print("5. Mostrar lista invertida")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Lista:", lista)
        elif opcion == "2":
            num = int(input("Ingrese el número a verificar: "))
            resultado = aparece_mas_veces_que_el_mayor(lista, num)
            print("¿Aparece más veces que el mayor?:", resultado)
        elif opcion == "3":
            print("Media total:", media_total(lista))
        elif opcion == "4":
            print("Media entre mayor y menor:", media_mayor_menor(lista))
        elif opcion == "5":
            print("Lista invertida:", lista_invertida(lista))
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()