from igraph import Graph

from metodos import gera_grafo_igraph
from algoritmo_indutivo import algoritmo_indutivo, aplica_ativacao

grafo_bipartido = gera_grafo_igraph(Graph.Random_Bipartite(6,6, m = 21))

grafo_tree = gera_grafo_igraph(Graph.Tree(n=30, children=2))


grafo_grid = gera_grafo_igraph(Graph.Lattice(dim=[4,4]))
n = 10
contagem = 0
print(grafo_bipartido)
for i in range(n):
    result = algoritmo_indutivo(grafo_bipartido)
    if aplica_ativacao(grafo_bipartido, result):
        contagem += 1
        print("correto: ", result)
    else:
        print("errado: ", result)

print("resultado: ", contagem / n)
print("\n")
contagem = 0
print(grafo_tree)
for i in range(n):
    result = algoritmo_indutivo(grafo_tree)
    if aplica_ativacao(grafo_tree, result):
        contagem += 1
        print("correto: ", result)
    else:
        print("errado: ", result)

print("tree: ", contagem / n)
print("\n")

contagem = 0
print(grafo_grid)
for i in range(n):
    result = algoritmo_indutivo(grafo_grid)
    if aplica_ativacao(grafo_grid, result):
        contagem += 1
        print("correto: ", result)
    else:
        print("errado: ", result)

print("tree: ", contagem / n)
print("\n")