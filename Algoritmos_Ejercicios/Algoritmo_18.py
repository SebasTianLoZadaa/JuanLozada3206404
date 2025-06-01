# Algoritmo para calcular la letra de control del NIT

# Tabla de letras según el residuo de dividir el NIT entre 23
letras_control = [
    "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
    "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"
]

# Solicitar el número de NIT al usuario
try:
    nit = int(input("Ingrese el número de NIT (sin letra): "))
    resto = nit % 23
    letra = letras_control[resto]
    print(f"La letra de control para el NIT {nit} es: {letra}")
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
