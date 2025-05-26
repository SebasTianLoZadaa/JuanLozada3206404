#Programa para encontrar la media de la lista 
import random
j = [random.randint(1,100) for _ in range (20)]
print ("Lista Generada:", j)

media = sum (j) / len(j)
print(f"La media de los numeros de la lista es: {media:.2f}")

try: 
    nb = int(input("Ingrese el numero a buscar:")) 
    if nb < 1:
        print("el numero tiene que ser mayor a 0")
    else:
        if nb in j:
            p = j.index (nb)
            print(f"numero encontrado en la posicion {p}")
        else:
            print("numero no encontrado")
except ValueError :
    print("Debe ingresar un numero valido")
