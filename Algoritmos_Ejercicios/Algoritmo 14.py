def contar_palabras(texto):
    palabras = texto.split()
    cantidad = len(palabras)
    palabra_mas_larga = max(palabras, key=len) if palabras else ""
    return cantidad, len(palabra_mas_larga)