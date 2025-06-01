import random

digitos_objetivo = random.sample(range(10), 4)
#print("DEBUG: Dígitos a adivinar:", digitos_objetivo)  # Puedes quitar esta línea luego

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
    
    pista = []
    for i in range(4):
        if intento[i] == digitos_objetivo[i]:
            pista.append("verde")
        elif intento[i] in digitos_objetivo:
            pista.append("amarillo")
        else:
            pista.append("rojo")
    
    print("Pista:", pista)
    
    if pista == ["verde", "verde", "verde", "verde"]:
        print(f"¡Felicidades! Adivinaste los dígitos en {intentos} intentos.")
        break
