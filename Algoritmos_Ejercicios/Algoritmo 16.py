def calcular_cambio(valor_cobrar, monto_entregado):
    cambio = monto_entregado - valor_cobrar
    if cambio < 0:
        return "Monto insuficiente"
    monedas = [1000, 500, 200, 100, 50]
    resultado = {}
    for moneda in monedas:
        cantidad = cambio // moneda
        if cantidad:
            resultado[moneda] = cantidad
            cambio %= moneda
    return resultado