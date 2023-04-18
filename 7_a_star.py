from collections import deque

def a_star(inicio, meta, grafo):
    cola = deque() #Lista
    visitados = set() #Coleccion
    nodo_padre = {}
    cola.append(inicio) # Tupla con el nodo y su costo acumulado
    visitados.add(inicio)
    mejor_costo = float("inf")

    while cola:
        
        actual = cola.popleft()
        if actual == meta:
            return visitados # Funcion para solucion

        nodo_siguiente = None
        for arista in grafo(actual):
            costo_distancia_heuristico = arista[1] + grafo(arista[0], "Heuristic")
            
            if costo_distancia_heuristico < mejor_costo: #Se busca el mejor costo total
                mejor_costo = costo_distancia_heuristico
                nodo_siguiente = arista[0] #se encontro el siguiente nodo
                #despues expandimos con su costo o si ya se visito expandimos por su bajo costo
            
        if nodo_siguiente not in visitados:
            visitados.add(nodo_siguiente)
            cola.append(nodo_siguiente)
            nodo_padre[nodo_siguiente] = actual
        elif nodo_siguiente in visitados:
            cola.append(nodo_siguiente)
        #CONTINUARA! 
        """
        Si ya esta en visitados, y el mejor_costo es mayor que el mejor_costo_anterior, 
        entonces
        hay que hacer actual(mejor_costo_anterior) y expandir
        """
        print(cola)
        print(visitados)
        print(mejor_costo)
    
    return None

def solucion_constructor():
    return None

def data(nodo, heuristic = None):
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
    
    if heuristic:
        return heuristica[nodo]

    return grafo[nodo]

inicio = 'A'
meta = 'H'
resultado = a_star(inicio, meta, data)
print(resultado)