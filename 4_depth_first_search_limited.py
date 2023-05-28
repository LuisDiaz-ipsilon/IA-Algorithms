from collections import deque
"""
DFSL version iterativa
Se agrego la varible profundidad que determina si detener el algoritmo dependiendo del valor 
"""
def dfsl(inicio, meta, data, profundidad):
    s = []
    s.append(inicio)
    visitados = set()
    ruta_sol = []


    while s:
        if profundidad <=0:
            return "La profundidad ya fue superada, ingrese una profundidad mayor"

        v = s.pop()
        ruta_sol.append(v)

        #En el caso de que si se encuentre v en visitados entonces se continua con pop para s hasta encontrar uno que no este en visitados
        if v not in visitados:
            visitados.add(v)
            profundidad -= 1
            if v == meta:
                return ruta_sol
            for arista in data(v):
                s.append(arista)
        
    return None

def data(nodo):

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
meta = 'F'
profundidad = 1
resultado = dfsl(inicio, meta, data, profundidad)
print("Este algoritmo es el DFS iterativo, por lo que el orden es inverso comenzando por los nodos de la derecha en su busqueda")
print(resultado)