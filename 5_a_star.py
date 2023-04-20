from collections import deque

def a_star(inicio, meta, grafo):
    cola = deque() #Lista
    visitados = set() #Coleccion
    nodo_padre = {}
    cola.append(inicio) # Tupla con el nodo y su costo acumulado
    visitados.add(inicio)
    mejor_costo = float("inf")
    visitados_costo_t = {} # Diccionario para almacenar el costo acumulado total D + H
    visitados_costo_t[inicio] = 0 + grafo(inicio, "Heuristic")

    while cola:
        """print(cola)
        print(visitados)
        print(mejor_costo)
        print(visitados_costo_t)"""
        
        actual = cola.popleft()

        if actual == meta:
            return solucion_constructor(inicio, meta, nodo_padre) # Funcion para solucion

        nodo_siguiente = None
        for arista in grafo(actual):
            costo_distancia_heuristico = arista[1] + grafo(arista[0], "Heuristic")
            
            if costo_distancia_heuristico < mejor_costo and arista[0] not in visitados: #Se busca el mejor costo total
                mejor_costo = costo_distancia_heuristico
                nodo_siguiente = arista[0] #se encontro el siguiente nodo
                #despues expandimos con su costo o si ya se visito expandimos por su bajo costo
            
        if nodo_siguiente == None:
            #Si no se encuentra un mejor nodo entonces retrocedemos al padre y eliminamos la arista del grafo
            nodo_siguiente = nodo_padre[actual]
            mejor_costo = visitados_costo_t[nodo_siguiente]  
        if nodo_siguiente not in visitados:
            visitados.add(nodo_siguiente)
            cola.append(nodo_siguiente)
            nodo_padre[nodo_siguiente] = actual
            visitados_costo_t[nodo_siguiente] = mejor_costo
        elif nodo_siguiente in visitados: 
            cola.append(nodo_siguiente)

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
resultado = a_star(inicio, meta, data)
print(resultado)