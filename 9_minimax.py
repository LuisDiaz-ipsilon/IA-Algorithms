from collections import deque

def minimax(arr):
    # Caso base: si el arreglo está vacío, no hay más jugadas posibles
    if len(arr) == 0:
        return 0

    # Obtener la cantidad de elementos en el arreglo
    n = len(arr)

    # Verificar si es el turno del jugador máximo o mínimo
    state = (n % 2) == 0

    # Caso base: si solo queda un elemento, devolverlo
    if n == 1:
        return arr[0]

    # Inicializar el valor de la mejor jugada
    best_value = float('-inf') if state else float('inf')

    # Calcular todas las jugadas posibles y evaluarlas recursivamente
    for i in range(n):
        # Copiar el arreglo para no modificar el original durante la recursión
        new_arr = arr[:i] + arr[i+1:]

        #llamada recursiva
        value = minimax(new_arr)

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

