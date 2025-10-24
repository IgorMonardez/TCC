from igraph import Graph

from algoritmo_forca_bruta import algoritmo_forca_bruta
from metodos import gera_grafo_igraph, printa_resultados, gera_split

grafo_bipartido = gera_grafo_igraph(Graph.Random_Bipartite(6,6, m=21))

grafo_split,_,_ = gera_split(7,7,0.5)

grafo_split = gera_grafo_igraph(grafo_split)

grafo_tree = gera_grafo_igraph(Graph.Tree(n=14, children=2))

grafo_grid = gera_grafo_igraph(Graph.Lattice(dim=[3,4]))

# TODO: Grafo split
# TODO: Ver por que grafo grid está "demorando" tanto para ser feito

# print("-----------------bipartido---------------- ")
# _, tamanho_otimo = algoritmo_forca_bruta(grafo_bipartido)
# printa_resultados(grafo_bipartido, tamanho_otimo)
# print("-----------------tree---------------- ")
# _, tamanho_otimo = algoritmo_forca_bruta(grafo_tree)
# printa_resultados(grafo_tree, tamanho_otimo)
print("-----------------grid---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_grid)
printa_resultados(grafo_grid, tamanho_otimo)
print("-----------------split---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_split)
printa_resultados(grafo_split, tamanho_otimo)
