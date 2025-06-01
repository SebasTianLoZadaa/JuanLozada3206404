#Dado un número entero, indicar el número de dígitos de ese número 

IngN= int(input("Ingrese e digito que desea saber su longitud"))
#Convertir el numero a positivo
IngN=abs(IngN)
#Convertirlo a una cadena de caracteres en  vez de int
Cadena= str (IngN)
#Funcion len para contar los caracteres 
cantidadigitos= len(Cadena)
print("el numero tiene", cantidadigitos, "digitos")
