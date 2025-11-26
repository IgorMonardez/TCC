from igraph import Graph

from algoritmo_forca_bruta import algoritmo_forca_bruta
from metodos import gera_grafo_igraph, printa_resultados, gera_split

grafo_bipartido = {'0': [['6', '7', '8', '10'], False], '1': [['6', '7', '8', '10', '11'], True], '2': [['10', '11'], False], '3': [['8', '9', '11'], True], '4': [['6', '7', '11'], True], '5': [['7', '8', '9', '10'], False], '6': [['0', '1', '4'], True], '7': [['0', '1', '4', '5'], False], '8': [['0', '1', '3', '5'], False], '9': [['3', '5'], False], '10': [['0', '1', '2', '5'], False], '11': [['1', '2', '3', '4'], False]}


grafo_split = {'0': [['1', '2', '3', '4', '5', '6', '13'], True], '1': [['0', '2', '3', '4', '5', '6', '8', '10'], False], '2': [['0', '1', '3', '4', '5', '6', '8', '11'], False], '3': [['0', '1', '2', '4', '5', '6', '8', '12', '13'], True], '4': [['0', '1', '2', '3', '5', '6', '8', '10', '12', '13'], False], '5': [['0', '1', '2', '3', '4', '6', '8'], True], '6': [['0', '1', '2', '3', '4', '5', '7', '10', '11', '13'], False], '7': [['6'], True], '8': [['1', '2', '3', '4', '5'], True], '9': [[], False], '10': [['1', '4', '6'], True], '11': [['2', '6'], False], '12': [['3', '4'], False], '13': [['0', '3', '4', '6'], False]}

grafo_tree = {'0': [['1', '2'], False], '1': [['0', '3', '4'], True], '2': [['0', '5', '6'], True], '3': [['1', '7', '8'], True], '4': [['1', '9', '10'], True], '5': [['2', '11', '12'], True], '6': [['2', '13'], False], '7': [['3'], True], '8': [['3'], True], '9': [['4'], True], '10': [['4'], True], '11': [['5'], True], '12': [['5'], True], '13': [['6'], True]}

grafo_grid = {'0': [['1', '2', '3', '9'], False], '1': [['0', '2', '4', '10'], False], '2': [['0', '1', '5', '11'], False], '3': [['0', '4', '5', '6'], False], '4': [['1', '3', '5', '7'], False], '5': [['2', '3', '4', '8'], False], '6': [['3', '7', '8', '9'], False], '7': [['4', '6', '8', '10'], False], '8': [['5', '6', '7', '11'], False], '9': [['0', '6', '10', '11'], False], '10': [['1', '7', '9', '11'], False], '11': [['2', '8', '9', '10'], False]}


# TODO: Grafo split
# TODO: Ver por que grafo grid está "demorando" tanto para ser feito

print("-----------------bipartido---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_bipartido)
printa_resultados(grafo_bipartido, tamanho_otimo)
print("-----------------tree---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_tree)
printa_resultados(grafo_tree, tamanho_otimo)
print("-----------------grid---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_grid)
printa_resultados(grafo_grid, tamanho_otimo)
print("-----------------split---------------- ")
_, tamanho_otimo = algoritmo_forca_bruta(grafo_split)
printa_resultados(grafo_split, tamanho_otimo)
