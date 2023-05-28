from collections import deque

def minimax_alphabeta(arr):
    #  Si el arreglo está vacío, no hay más jugadas posibles
    if len(arr) == 0:
        return 0

    # Obtener la cantidad de elementos en el arreglo
    n = len(arr)

    # Se crea variable estado para determinar si sige min o max
    state = (n % 2) == 0

    # Si solo hay un elemento en el arreglo esa seria la respuesta
    if n == 1:
        return arr[0]

    # Inicializar los valores de alfa y beta
    alpha = float('-inf')
    beta = float('inf')

    # Calcular todas las jugadas posibles y evaluarlas recursivamente
    for i in range(n):
        # Copiar el arreglo para no modificar el original durante la recursión
        new_arr = arr[:i] + arr[i+1:]

        #llamada recursiva
        value = minimax_alphabeta(new_arr)

        # Actualizar el valor de la mejor jugada según el turno del jugador
        if state:
            alpha = max(alpha, value)
        else:
            beta = min(beta, value)

        # Realizar poda Alfa-Beta
        if alpha >= beta:
            print("poda")
            break

    return alpha if state else beta



arr = [4,48,15,25,36,23,19,-5,-25,11,-46,7,45,-9,48,10]
resultado = minimax_alphabeta(arr)
print(resultado)