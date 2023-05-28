from collections import deque

def bfs(inicio, meta, grafo):
    cola = deque() #Lista
    visitados = set() #Coleccion
    nodo_padre = {}
    cola.append(inicio)
    visitados.add(inicio)
    
    while cola: #La cola siempre contendra un nodo asi que estara siempre en el ciclo hasta encontrar la meta
        
        actual = cola.popleft() #Se toma y elimina el primer elemento.
        print(actual)
        if actual == meta:  #En caso de que se llege a la meta se crea el arreglo del recorrido
            return nodos_solucion(nodo_padre, inicio, meta)
        for arista in grafo(actual): #Se hace la busqueda de los aristas hasta estar en 
            if arista not in visitados:
                visitados.add(arista)
                nodo_padre[arista] = actual
                cola.append(arista)

    
    return None

#Genera un arreglo con la solucion.
"""
nodo_padre: es un arreglo donde los indices son los nodos y el valor que contiene es el nodo_padre
inicio: nodo inicial
meta: nodo final
"""
def nodos_solucion(nodo_padre, inicio, meta):
    camino = [meta]
    actual = meta
    while actual != inicio:
        actual = nodo_padre[actual] #retroceso
        camino.insert(0, actual)
    return camino

def test(nodo):
    # Ejemplo de función que retorna los aristas de un nodo
    # representado como lista de adyacencia:
    # de esta manera cuando se pregunte por un nodo se devolvera las aristas de los nodos a los cuales esta conectado
    # incluyendo el padre.
    grafo = {'A': ['B', 'C', 'D'],
             'B': ['A', 'E', 'F'],
             'C': ['A'],
             'D': ['A', 'G',  'H'],
             'E': ['B'],
             'F': ['B'],
             'G': ['D'],
             'H': ['D']}
    return grafo[nodo]

inicio = 'A'
meta = 'G'
resultado = bfs(inicio, meta, test)
print(resultado)
