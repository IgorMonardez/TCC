import random
from collections import Counter


def vizinhanca(grafo, vertice):
    return grafo[vertice][0]


def estado_vertice(grafo, vertice):
    return grafo[vertice][1]


def retira_vizinhanca_fechada(grafo, vertice_removido):
    vertices_remover = grafo[vertice_removido][0] + [vertice_removido]

    novo_grafo = {}
    for vertice, (vizinhos, estado) in grafo.items():
        if vertice not in vertices_remover:
            vizinhanca = list(set(vizinhos) - set(vertices_remover))
            novo_grafo[vertice] = [vizinhanca, estado]

    return novo_grafo


def retira_vertice(grafo, vertice_removido):
    if vertice_removido not in grafo:
        return grafo

    novo_grafo = {}
    for vertice, (vizinhos, estado) in grafo.items():
        if vertice != vertice_removido:
            novos_vizinhos = [v for v in vizinhos if v != vertice_removido]
            novo_grafo[vertice] = [novos_vizinhos, estado]

    return novo_grafo


def procura_vertice_grau_par(grafo):
    for vertice in grafo:
        if len(vizinhanca(grafo, vertice)) % 2 == 0:
            return vertice


def aplica_ativacao(grafo, ativacao):
    vertices_grafos = list(grafo.keys())

    for vertice in vertices_grafos:
        grafo[vertice][1] = True

    for vertice in ativacao:
        if grafo[vertice][1]:
            grafo[vertice][1] = False
        else:
            grafo[vertice][1] = True
        for vizinho in vizinhanca(grafo, vertice):
            if grafo[vizinho][1]:
                grafo[vizinho][1] = False
            else:
                grafo[vizinho][1] = True

    for vertice in vertices_grafos:
        if grafo[vertice][1]:
            return False

    return True


def uniao(s1, s2):
    s = set()

    for i in s1:
        if i not in s2:
            s.add(i)

    for i in s2:
        if i not in s1 and i not in s:
            s.add(i)

    return s



def algoritmo_indutivo(grafo):
    vertices = list(grafo.keys())
    random.shuffle(vertices)
    n = len(vertices)
    if n == 0:
        return list()

    if n == 1:
        return [list(grafo.keys())[0]]
    v = 0
    solucao_v = []
    for v in vertices:
        grafo_v = retira_vertice(grafo, v)
        solucao_v = algoritmo_indutivo(grafo_v)
        if aplica_ativacao(grafo, solucao_v):
            return solucao_v

    if n % 2 == 0:
        solucao = solucao_v.copy()
        vertices_v = vertices.copy()
        vertices_v.remove(v)
        for w in vertices_v:
            grafo_w = retira_vertice(grafo, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            solucao = uniao(solucao, solucao_w)

        return solucao
    else:
        v = procura_vertice_grau_par(grafo)
        grafo_v = retira_vizinhanca_fechada(grafo, v)
        solucao = [v]
        for w in grafo_v:
            grafo_w = retira_vertice(grafo, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            solucao = uniao(solucao, solucao_w)

        return solucao


#TODO: Algumas dúvidas, como a ordem da solução e de como fazer a união das soluções.
if __name__ == '__main__':

    grafo_simples = {
        '1': [['2', '3', '4'], True],
        '2': [['1'], True],
        '3': [['1'], True],
        '4': [['1'], True]
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

    n = 1000
    contagem = 0
    for i in range(n):
        result = algoritmo_indutivo(grafo_split)
        if aplica_ativacao(grafo_split, result):
            contagem += 1
            print("correto: ", result)
        else:
            print("errado: ", result)

    print("split: ",contagem / n)

    n = 1000
    contagem = 0
    for i in range(n):
        result = algoritmo_indutivo(grafo_bipartido)
        if aplica_ativacao(grafo_bipartido, result):
            contagem += 1
            print("correto: ", result)
        else:
            print("errado: ", result)

    print("bipartido: ",contagem / n)

    n = 1000
    contagem = 0
    for i in range(n):
        result = algoritmo_indutivo(grafo_tree)
        if aplica_ativacao(grafo_tree, result):
            contagem += 1
            print("correto: ", result)
        else:
            print("errado: ", result)

    print("tree: ",contagem / n)
