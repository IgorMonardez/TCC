import copy
from random import random

from igraph import Graph
from algoritmo_forca_bruta import algoritmo_forca_bruta
from algoritmo_guloso import algoritmo_guloso
from algoritmo_indutivo import algoritmo_indutivo,aplica_ativacao

def gera_grafo_igraph(grafo_igraf):
    grafo_dict = {}
    for vertice in range(grafo_igraf.vcount()):
        vizinhos = grafo_igraf.neighbors(vertice)
        for index, vizinho in enumerate(vizinhos):
            vizinhos[index] = str(vizinho)
        grafo_dict[str(vertice)] = [vizinhos, True]

    return grafo_dict

def gera_split(tam_clique, tam_is, prob):

    total_vertices = tam_clique + tam_is
    g = Graph()

    # Adicionar vértices
    g.add_vertices(total_vertices)

    # Criar o clique (todos conectados entre si)
    vertices_clique = list(range(tam_clique))
    for i in range(tam_clique):
        for j in range(i + 1, tam_clique):
            g.add_edge(i, j)

    # Criar conexões entre clique e conjunto independente
    vertices_independentes = list(range(tam_clique, total_vertices))

    for vertice_clique in vertices_clique:
        for vertice_independente in vertices_independentes:
            if random() < prob:
                g.add_edge(vertice_clique, vertice_independente)

    return g, vertices_clique, vertices_independentes



def printa_resultados(grafo, tamanho_otimo):
    n = 100
    grafo = copy.deepcopy(grafo)
    print(grafo)


    # print("guloso: ", resultado_guloso(grafo, n, tamanho_otimo))
    print("indutivo: ", resultado_indutivo(grafo, n, tamanho_otimo))

def calcula_optimalidade(tamanho_otimo, ativacao):
    if tamanho_otimo == len(ativacao):
        return True
    return False

def resultado_guloso(grafo, n, tam_otimo):
    contagem_corretude = 0
    contagem_optimidade = 0
    for i in range(n):
        result = algoritmo_guloso(grafo)
        if aplica_ativacao(grafo, result):
            contagem_corretude += 1
            if calcula_optimalidade(tam_otimo, result):
                contagem_optimidade += 1
                print("otimo: ", result)
            else:
                print("apenas correto: ", result)
        else:
            print("errado: ", result)

    optimidade = contagem_optimidade / n
    corretude = contagem_corretude / n
    return optimidade, corretude

def resultado_indutivo(grafo, n, tam_otimo):
    contagem_corretude = 0
    contagem_optimidade = 0
    for i in range(n):
        result = algoritmo_indutivo(grafo)
        if aplica_ativacao(grafo, result):
            contagem_corretude += 1
            if calcula_optimalidade(tam_otimo, result):
                contagem_optimidade += 1
                print("otimo: ", result)
            else:
                print("apenas correto: ", result)
        else:
            print("errado: ", result)

    optimidade = contagem_optimidade / n
    corretude = contagem_corretude / n
    return optimidade, corretude
