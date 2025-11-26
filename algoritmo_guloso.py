import copy
import random
from collections import deque
from algoritmo_forca_bruta import algoritmo_forca_bruta
# from igraph import Graph


# from metodos import gera_grafo_igraph

def adiciona_vertice(grafo, vertice, vizinhos):
    vizinhos = [v for v in vizinhos if v != vertice]

    vizinhos = list(dict.fromkeys(vizinhos))

    if vertice not in grafo:
        grafo[vertice] = [vizinhos, False]
    else:
        grafo[vertice][0] = vizinhos

    for vizinho in vizinhos:
        if vizinho not in grafo:
            grafo[vizinho] = [[], False]
        if vertice not in grafo[vizinho][0]:
            grafo[vizinho][0].append(vertice)

    return grafo


def verifica_ativacao(ativacao, grafo, v):
    vizinhos = grafo[v][0]
    contagem = 0
    for vizinho in vizinhos:
        if vizinho in ativacao:
            contagem += 1

    if contagem % 2 == 0:
        ativacao.append(v)
    return ativacao


def muda_estado_vizinhanca(grafo, v):
    vizinhos = grafo[v][0]

    grafo[v][1] = not grafo[v][1]

    for vizinho in vizinhos:
        grafo[vizinho][1] = not grafo[vizinho][1]
    return grafo


def procura_vertice_ligado(grafo):
    items = list(grafo.keys())
    random.shuffle(items)
    for vertice in items:
        if grafo[vertice][1]:
            return vertice

    return None


def reversao_vizinhanca(grafo, v):
    if v not in grafo:
        return

    # Obtém a lista de vizinhos do vértice v (primeiro elemento do array de valor)
    vizinhos = grafo[v][0].copy()  # Fazemos uma cópia para evitar modificar durante iteração
    n = len(vizinhos)

    for i in range(n):
        for j in range(i + 1, n):
            v1 = vizinhos[i]
            v2 = vizinhos[j]

            # Verifica se v2 é vizinho de v1
            if v2 in grafo[v1][0]:
                # Remove a aresta entre v1 e v2 (ambas as direções)
                grafo[v1][0].remove(v2)
                grafo[v2][0].remove(v1)
            else:
                # Adiciona aresta entre v1 e v2 (ambas as direções)
                grafo[v1][0].append(v2)
                grafo[v2][0].append(v1)
    return grafo
def retira_vertice(grafo, vertice_removido):
    if vertice_removido not in grafo:
        return grafo

    novo_grafo = {}
    for vertice, (vizinhos, estado) in grafo.items():
        if vertice != vertice_removido:
            novos_vizinhos = [v for v in vizinhos if v != vertice_removido]
            novo_grafo[vertice] = [novos_vizinhos, estado]

    return novo_grafo

def algoritmo_guloso(grafo):
    novo_grafo = copy.deepcopy(grafo)
    novo_grafo, pilha = fase_1(novo_grafo)
    ativacao = fase_2(novo_grafo, pilha)
    return ativacao

def inicializa_grafo(grafo):
    for vertice,_ in grafo.items():
        grafo[vertice][1] = True

    return grafo

def fase_1(grafo):
    pilha = deque()
    grafo = inicializa_grafo(grafo)
    v = procura_vertice_ligado(grafo)
    while v is not None:
        pilha.append([v, grafo[v][0]])

        grafo = muda_estado_vizinhanca(grafo, v)

        grafo = reversao_vizinhanca(grafo, v)

        grafo = retira_vertice(grafo, v)

        v = procura_vertice_ligado(grafo)

    return grafo, pilha


def fase_2(grafo, pilha):
    ativacao = []

    while pilha:
        vertice, vizinhos = pilha.pop()

        grafo = adiciona_vertice(grafo, vertice, vizinhos)

        grafo = reversao_vizinhanca(grafo, vertice)

        ativacao = verifica_ativacao(ativacao, grafo, vertice)

    return ativacao


if __name__ == '__main__':
    grafo_simples = {
        '1': [['2', '6'], True],
        '2': [['1', '3'], True],
        '3': [['2', '4'], True],
        '4': [['3', '5'], True],
        '5': [['4', '6'], True],
        '6': [['5', '1'], True]
    }

    grafo_split = {
        '1': [['2', '3', '6'], True],
        '2': [['1', '3', '4'], True],
        '3': [['1', '2', '5'], True],
        '4': [['2'], True],
        '5': [['3'], True],
        '6': [['1'], True]
    }

    grafo_bipartido = {
        '1': [['a', 'b'], True],
        '2': [['a', 'b', 'c'], True],
        '3': [['c'], True],
        'a': [['1', '2'], True],
        'b': [['1', '2'], True],
        'c': [['3', '2'], True],
    }

    grafo_tree = {
        '1': [['2', '3'], True],
        '2': [['1', '4'], True],
        '3': [['1', '5'], True],
        '4': [['2'], True],
        '5': [['3'], True],
    }
    # grafo_tree = gera_grafo_igraph(Graph.Tree(n=15, children=3))
    _, tam_otimo = algoritmo_forca_bruta(grafo_tree)
    for i in range(10):
        print(grafo_tree)
        print(algoritmo_guloso(grafo_tree))
