#programa para crear una lista que invierta la primera 
import random

l = [random.randint (1, 100) for _ in range (20) ]
print ("lista original:", l)

#crear lista inversa 
l_inversa = l [:: -1]
print ("lista inversa :", l_inversa ) 

try:
    nb= int(input("Ingrese el numero a buscar: "))
    if nb <1:
        print ("El numero debe ser mayor a 0")
    else:
        if nb in l:
            p= l.index (nb)
            print (f"Numero encontrado en la posicion {p}")
        else:
         print("Numero no encontrado")
except ValueError:
    print("Debe ingresar un numero entero")
    
