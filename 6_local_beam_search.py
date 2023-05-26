from collections import deque

def beam_search(inicio, meta, grafo, beam_width):
    cola = deque()  # Lista
    visitados = set()  # Coleccion
    nodo_padre = {}
    cola.append((inicio, 0))  # Tupla con el nodo y su costo acumulado
    visitados.add(inicio)

    while cola:
        cola = sorted(cola, key=lambda x: x[1])[:beam_width]  # Reducir la cola al ancho deseado
        nuevos_nodos = []

        while cola:
            actual, costo_acumulado = cola.pop(0)

            if actual == meta:
                return solucion_constructor(inicio, meta, nodo_padre)  # Funcion para obtener la solucion

            for arista in grafo(actual):
                nodo_siguiente = arista[0]
                costo_arista = arista[1]
                costo_total = costo_acumulado + costo_arista

                if nodo_siguiente not in visitados:
                    visitados.add(nodo_siguiente)
                    nuevos_nodos.append((nodo_siguiente, costo_total))
                    nodo_padre[nodo_siguiente] = actual

        cola.extend(nuevos_nodos)

    return "Finalizado"

def solucion_constructor(inicio, meta, nodos_padre):
    camino = [meta]
    nodo = meta
    while nodo != inicio:
        nodo = nodos_padre[nodo]
        camino.append(nodo)
    camino.reverse()
    return camino

def data(nodo, instruccion = None):
    """
    Contemos un grafo con costo y una tabla con la heuristica:
    """
    grafo = {'A': [('B', 1), ('C', 4), ('D', 2)],
            'B': [('A', 1), ('E', 8), ('F', 3)],
            'C': [('A', 4)],
            'D': [('A', 2), ('G', 5), ('H', 1)],
            'E': [('B', 8)],
            'F': [('B', 3)],
            'G': [('D', 5)],
            'H': [('D', 1)]}
    
    heuristica = {
            'A': 23,
            'B': 12,
            'C': 8,
            'D': 14,
            'E': 9,
            'F': 11,
            'G': 7,
            'H': 0}
    
    if instruccion == "Heuristic": #Retornar valor heuristico
        return heuristica[nodo]
    elif instruccion == "Del": #Eliminar 
        del grafo[nodo]
        del heuristica[nodo]
        for nodo, aristas in grafo.items():
            for arista in aristas:
                if arista[0] == nodo:
                    aristas.remove(arista)
        for nodo, aristas in grafo.items():
            print(nodo)
            print(aristas)
                    
            

    return grafo[nodo] #Retornar solo el nodo

inicio = 'A'
meta = 'H'
beam_width = 1 #Número de mejores nodos que se mantendrán en cada paso
resultado = beam_search(inicio, meta, data, beam_width)
print(resultado)