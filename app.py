# recibe los parametros: el array a ordenar, el indice mas bajo y el mas alto
def quicksort(array, low=0, high=None):
    # si high no se pasa, se toma como el ultimo indice del array
    if high is None:
        high = len(array) - 1
    # si el indice mas bajo es menor al mas alto
    if low < high:
        
        # se obtiene el indice del pivote
        pivot_index = partition(array, low, high)

        # se ordenan los elementos a la izquierda y derecha del pivote
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

def partition(array, low, high):
    
    # se toma el pivote
    pivot = array[high]
    
    # indicador para los elementos menores o iguales al pivote
    i = low - 1

    for j in range(low, high):
        # si el elemento es menor o igual al pivote
        if array[j] <= pivot:
            # se incrementa el indicador y se intercambian los elementos
            i += 1
            array[i], array[j] = array[j], array[i]
    # se intercambia el pivote con el elemento en la posicion i+1 
    array[i+1], array[high] = array[high], array[i+1]

    # se devuelve la posicion del pivote
    return i+1



lista1 = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(lista1)
print(lista1)
lista2 = [2, 6, 4, 2, 4, 5, 10, 1]
quicksort(lista2)
print(lista2)

