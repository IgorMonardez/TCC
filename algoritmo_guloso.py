import random


def adiciona_vertice(grafo, v):
    grafo[v[0]][0] = v[1]
    for vizinho in v[1]:
        grafo[v[0]][0] += vizinho
    return grafo

def verifica_ativacao(ativacao, grafo, v):
    vizinhos = grafo[v]
    contagem = 0
    for vertice_ativado in ativacao:
        if vertice_ativado in vizinhos:
            contagem+=1

    if contagem % 2 == 0:
        ativacao += v
    return ativacao


def muda_estado_vizinhanca(grafo, v):
    if grafo[v][1]:
        grafo[v][1] = False
    else:
        grafo[v][1] = True
    for vizinho in grafo[v][0]:
        if grafo[vizinho][1]:
            grafo[vizinho][1] = False
        else:
            grafo[vizinho][1] = True
    return grafo

def procura_vertice_ligado(grafo):
    items = list(grafo.keys())
    random.shuffle(items)
    for vertice in items:
        if grafo[vertice][1]:
            return vertice
    return None

def reversao_vizinhanca(grafo, v):
    vizinhos_v = grafo[v][0]

    for vizinho1 in vizinhos_v:
        for vizinho2 in vizinhos_v:
            if vizinho2 in grafo[vizinho1][0]:
                grafo[vizinho1][0].remove(vizinho2)
                grafo[vizinho2][0].remove(vizinho1)
            else:
                grafo[vizinho1][0]+=[vizinho2]
                grafo[vizinho2][0]+=[vizinho1]
    return grafo

def retira_vertice(grafo, vertice_removido):
    if vertice_removido not in grafo:
        return grafo

    for vertice, (vizinhos, estado) in grafo.items():
        if vertice != vertice_removido:
            novos_vizinhos = [v for v in vizinhos if v != vertice_removido]
            grafo[vertice] = [novos_vizinhos, estado]
    return grafo

def algoritmo_guloso(grafo):
    pilha = fase_1(grafo)
    ativacao = fase_2(grafo,pilha)
    return ativacao


def fase_1(grafo):
    pilha = []
    v = procura_vertice_ligado(grafo)
    while v is not None:
        pilha += [[v,grafo[v][0]]]

        grafo = muda_estado_vizinhanca(grafo, v)

        grafo = reversao_vizinhanca(grafo, v)

        grafo = retira_vertice(grafo, v)

        v = procura_vertice_ligado(grafo)

    return pilha


def fase_2(grafo, pilha):
    ativacao = []
    pilha.reverse()
    for vertice, vizinhos in pilha:
        adiciona_vertice(grafo, (vertice,vizinhos))

        reversao_vizinhanca(grafo, vertice)

        return verifica_ativacao(ativacao, grafo, vertice)

if __name__ == '__main__':
    grafo_simples = {
        '1': [['2', '6'], True],
        '2': [['1','3'], True],
        '3': [['2','4'], True],
        '4': [['3','5'], True],
        '5': [['4','6'], True],
        '6': [['5','1'], True]
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

    print(algoritmo_guloso(grafo_split))

