from collections import deque

def uniform_cost_search(inicio, meta, grafo):
    cola = deque() #Lista
    visitados = set() #Coleccion
    nodo_padre = {}
    visitados_costo = {} # Diccionario para almacenar el costo acumulado de cada nodo
    cola.append((inicio, 0)) # Tupla con el nodo y su costo acumulado
    visitados.add(inicio)

    while cola:
        actual, costo_acumulado = cola.popleft()
        if actual == meta:
            # Para dar solucion se lee el padre establecido de la meta, y se continua iterando para cada nodo padre
            camino = [meta]
            nodo = meta
            while nodo != inicio:
                nodo = nodo_padre[nodo]
                camino.append(nodo)
            camino.reverse() #la lista estara ordenada desde la meta hasta el inicio, por lo que se usa el reverse
            return camino

        for arista in grafo(actual):
            nodo_siguiente = arista[0]
            costo_arista = arista[1]

            if nodo_siguiente not in visitados: #primero abrimos los nodos excepto el padre y visitados
                nuevo_costo_acumulado = costo_acumulado + costo_arista
                #despues expandimos con su costo o si ya se visito expandimos por su bajo costo
                if nodo_siguiente not in visitados_costo or nuevo_costo_acumulado < visitados_costo[nodo_siguiente]:
                    visitados_costo[nodo_siguiente] = nuevo_costo_acumulado
                    nodo_padre[nodo_siguiente] = actual
                    visitados.add(nodo_siguiente)
                    cola.append((nodo_siguiente, nuevo_costo_acumulado))

    return None

def test(nodo):
    """
    para cada nodo se agrego la arista junto con costo
    imagen: grafo_costo_ejemplo.png
    """
    grafo = {'A': [('B', 1), ('C', 4), ('D', 2)],
            'B': [('A', 1), ('E', 8), ('F', 3)],
            'C': [('A', 4)],
            'D': [('A', 2), ('G', 5), ('H', 1)],
            'E': [('B', 8)],
            'F': [('B', 3)],
            'G': [('D', 5)],
            'H': [('D', 1)]}
    return grafo[nodo]

inicio = 'A'
meta = 'H'
resultado = uniform_cost_search(inicio, meta, test)
print(resultado)
