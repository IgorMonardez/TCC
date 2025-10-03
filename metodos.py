
def gera_grafo_igraph(grafo_igraf):
    grafo_dict = {}
    for vertice in range(grafo_igraf.vcount()):
        vizinhos = grafo_igraf.neighbors(vertice)
        for index, vizinho in enumerate(vizinhos):
            vizinhos[index] = str(vizinho)
        grafo_dict[str(vertice)] = [vizinhos, True]

    return grafo_dict
