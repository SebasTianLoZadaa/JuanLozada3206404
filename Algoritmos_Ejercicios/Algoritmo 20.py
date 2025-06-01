#Calcular los pagos mensuales de una hipoteca y el total a pagar. El programa debe solicitar el x 

capital = float(input("Ingrese el capital del préstamo: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
años = int(input("Ingrese el número de años del préstamo: "))

tasa_mensual = interes_anual / (12 * 100)
numero_pagos = años * 12

cuota_mensual = (capital * tasa_mensual) / (1 - (1 + tasa_mensual) ** (-numero_pagos))
total_pagar = cuota_mensual * numero_pagos

print(f"Cuota mensual a pagar: {cuota_mensual:.2f}")
print(f"Total a pagar en {años} años: {total_pagar:.2f}")
