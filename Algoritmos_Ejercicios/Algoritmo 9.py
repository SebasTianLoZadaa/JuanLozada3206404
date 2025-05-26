def aparece_mas_veces_que_el_mayor(lista, numero):
    apariciones_numero = lista.count(numero)
    mayor = max(lista)
    apariciones_mayor = lista.count(mayor)
    return apariciones_numero > apariciones_mayor