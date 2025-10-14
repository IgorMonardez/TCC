from igraph import Graph

from metodos import gera_grafo_igraph, printa_resultados

grafo_bipartido = gera_grafo_igraph(Graph.Random_Bipartite(7,7, m = 30))

grafo_tree = gera_grafo_igraph(Graph.Tree(n=15, children=3))

grafo_grid = gera_grafo_igraph(Graph.Lattice(dim=[3,3]))

# TODO: Grafo split
# TODO: Ver por que grafo grid está "demorando" tanto para ser feito

# print("-----------------bipartido---------------- ")
# printa_resultados(grafo_bipartido)
# print("-----------------tree---------------- ")
# printa_resultados(grafo_tree)
print("-----------------grid---------------- ")
printa_resultados(grafo_grid)
