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


def procura_vertice_par(grafo):
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


def algoritmo_indutivo(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)
    # print('n: ', n)
    if n == 0:
        return set()
    v = random.choice(vertices)
    # print('v: ', v)
    if n == 1:
        return {list(grafo.keys())[0]}

    grafo_v = retira_vertice(grafo, v)

    solucao_v = algoritmo_indutivo(grafo_v)

    if aplica_ativacao(grafo, solucao_v):
        # print(f"aplicado: {solucao_v}")
        return solucao_v

    if n % 2 == 0:
        # print("par")
        solucao = []
        for w in grafo_v:
            # print('w: ', w)
            grafo_w = retira_vertice(grafo, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            solucao = solucao_w ^ solucao_v

        return solucao
    else:
        # print("impar")
        v = procura_vertice_par(grafo)
        grafo_v = retira_vizinhanca_fechada(grafo, v)
        solucao = {v}
        for w in grafo_v:
            # print('w: ', w)
            grafo_w = retira_vertice(grafo_v, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            solucao = solucao.union(solucao_w)

        return solucao


#TODO: Algumas dúvidas, como a ordem da solução e de como fazer a união das soluções.
if __name__ == '__main__':
    grafo = {
        '1': [['2', '3'], True],
        '2': [['1', '3', '4'], True],
        '3': [['1', '2'], True],
        '4': [['2'], True]
    }

    contagem = 0
    # grafo1 = {
    #     '1': [['a', 'b'], True],
    #     '2': [['a', 'b', 'c'], True],
    #     '3': [['c'], True],
    #     'a': [['1', '2'], True],
    #     'b': [['1', '2'], True],
    #     'c': [['3', '2'], True],
    # }
    n = 1000
    for i in range(n):
        result = algoritmo_indutivo(grafo)
        if aplica_ativacao(grafo, result):
            contagem += 1
            print("correto: ", result)
        else:
            print("errado: ", result)
    print(contagem / n)
