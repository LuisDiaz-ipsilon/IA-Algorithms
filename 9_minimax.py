from collections import deque

def minimax(arr):
    #print(arr[0])
    # Si el arreglo está vacío, no hay más jugadas posibles
    if len(arr) == 0:
        return 0

    # Obtener la cantidad de elementos en el arreglo
    n = len(arr)
    print(n)

    # Si solo hay un elemento en el arreglo esa seria la respuesta
    if n == 1:
        return arr[0]

    # Se crea variable estado para determinar si sige min o max
    state = (n % 2) == 0


    # Inicializar el valor de la mejor jugada
    best_value = float('-inf') if state else float('inf')
    

    # Calcular todas los valores posibles y evaluarlos recursivamente
    for i in range(n):
        
        # Copiar el arreglo para no modificar el original durante la recursión
        new_arr = arr[:i] + arr[i+1:]

        #llamada recursiva
        value = minimax(new_arr)
        #print(value)

        # Actualizar el valor depende del estado alfa o beta
        if state:
            best_value = max(best_value, value)
            
        else:
            best_value = min(best_value, value)

    return best_value

"""
MINIMAX:

"""
arr = [-3, 7, 2, -1, -7, -3, 8, 4]
resultado = minimax(arr)
print(resultado)

