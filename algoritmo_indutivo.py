import random


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
        grafo[vertice][1] = 1

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


def diferenca_simetrica(set_1, set_2):
    return set_1 ^ set_2


def algoritmo_indutivo(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)

    if n == 0:
        return set()

    if n == 1:
        return set(list(grafo.keys())[0])

    v = random.choice(vertices)
    grafo_v = retira_vertice(grafo, v)

    solucao_v = algoritmo_indutivo(grafo_v)

    if aplica_ativacao(grafo, solucao_v):
        return solucao_v

    if n % 2 == 0:
        vertices_v = vertices.copy()
        vertices_v.remove(v)
        paridade = {u: 0 for u in vertices}
        for w in vertices_v:
            grafo_w = retira_vertice(grafo, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            for u in solucao_w:
                paridade[u] = paridade[u] ^ 1

        return {u for u in vertices if paridade[u] == 1}
    else:
        v = procura_vertice_par(grafo)
        grafo_v = retira_vizinhanca_fechada(grafo, v)
        solucao = set()
        for w in grafo_v:
            grafo_w = retira_vertice(grafo, w)
            solucao_w = algoritmo_indutivo(grafo_w)
            solucao = diferenca_simetrica(solucao, solucao_w)

        result = {v}
        result = diferenca_simetrica(solucao, result)
        return result


if __name__ == '__main__':
    grafo = {
        '1': [['2', '3'], True],
        '2': [['1', '3', '4'], True],
        '3': [['1', '2', '5'], True],
        '4': [['2'], True],
        '5': [['3'], True]
    }
    contagem = 0
    for i in range(100):
        certo2 = {'1','2','3'}
        certo3 = {'3','2','1'}
        certo4 = {'2','3','1'}
        certo5 = {'2','1','3'}
        result = algoritmo_indutivo(grafo)
        if result == certo2:
            contagem += 1
        elif result == certo3:
            contagem += 1
        elif result == certo4:
            contagem += 1
        elif result == certo5:
            contagem += 1
        else:
            print(result)
    print(contagem/100)
