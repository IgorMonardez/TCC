import copy

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

def printa_resultados(grafo):
    n = 10
    contagem = 0
    grafo = copy.deepcopy(grafo)
    print(grafo)

    otimo, tamanho_otimo = algoritmo_forca_bruta(grafo)
    # print("guloso: ", resultado_guloso(grafo, n))
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
            print("apenas correto: ", result)
        else:
            print("errado: ", result)

    optimidade = contagem_optimidade / n
    corretude = contagem_corretude / n
    return optimidade, corretude
