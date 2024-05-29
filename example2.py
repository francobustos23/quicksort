def quicksort(lista):
    
    # si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # elegimos el pivote como el elemento del medio
    pivote = lista[len(lista) // 2]

    # dividimos la lista en tres partes
    # menores, iguales y mayores
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    # devolvemos la lista ordenada
    return quicksort(menores) + iguales + quicksort(mayores)

lista = [2, 6, 4, 2, 4, 5, 10, 1]
print(quicksort(lista))
lista2 = [64, 34, 25, 12, 22, 11, 90, 5]
print(quicksort(lista2))
