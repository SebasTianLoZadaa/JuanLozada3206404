import random

digitos_objetivo = random.sample(range(10), 4)
#print("DEBUG: Dígitos a adivinar:", digitos_objetivo)  # Elimínala para ocultar la respuesta

intentos = 0

while True:
    intentos += 1
    entrada = input("Ingrese 4 dígitos separados (ejemplo: 1 2 3 4): ")
    intento = entrada.split()
    
    if len(intento) != 4:
        print("Por favor ingrese exactamente 4 dígitos.")
        continue
    
    try:
        intento = [int(d) for d in intento]
    except ValueError:
        print("Por favor, ingrese solo números.")
        continue
    
    verdes = 0
    amarillos = 0
    rojos = 0

    for i in range(4):
        if intento[i] == digitos_objetivo[i]:
            verdes += 1
        elif intento[i] in digitos_objetivo:
            amarillos += 1
        else:
            rojos += 1
    
    print(f"Pista: Verdes: {verdes}, Amarillos: {amarillos}, Rojos: {rojos}")
    
    if verdes == 4:
        print(f"¡Ganaste! Adivinaste todos los dígitos en {intentos} intentos.")
        break
