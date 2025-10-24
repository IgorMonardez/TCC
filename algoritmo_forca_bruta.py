import random


def calcula_maior_grau(grafo):
    maior_grau = 0
    vertices = grafo.keys()
    for vertice in vertices:
        grau = len(grafo[vertice][0])
        if grau > maior_grau:
            maior_grau = grau

    return maior_grau


def ativa_grafo(grafo):
    for v in grafo.keys():
        grafo[v][1] = True


def verifica_ativacao(ativacao, grafo):
    vertices_ativacao = ativacao.keys()

    ativa_grafo(grafo)

    for v in vertices_ativacao:
        if grafo[v][1]:
            grafo[v][1] = False
        else:
            grafo[v][1] = True
        for vizinho in grafo[v][0]:
            if grafo[vizinho][1]:
                grafo[vizinho][1] = False
            else:
                grafo[vizinho][1] = True

    for v in grafo.keys():
        if grafo[v][1]:
            return False

    return True


def gera_subgrafos(grafo):
    vertices = list(grafo.keys())
    random.shuffle(vertices)
    n = len(vertices)
    min_subgraph = 9999999999999
    all_subgraphs = []
    for mask in range(1, 1 << n):
        subgraph_vertices = []
        vertex_index_map = {}

        for i in range(n):
            if mask & (1 << i):
                vertex = vertices[i]
                subgraph_vertices.append(vertex)
                vertex_index_map[vertex] = len(subgraph_vertices) - 1

        subgraph = {}
        for vertex in subgraph_vertices:
            neighbors = []
            for neighbor in grafo[vertex][0]:
                if neighbor in vertex_index_map:
                    neighbors.append(neighbor)
            subgraph[vertex] = neighbors
        all_subgraphs.append(subgraph)

    return all_subgraphs


def algoritmo_forca_bruta(grafo):
    maior_grau = calcula_maior_grau(grafo)
    subgrafos = gera_subgrafos(grafo)
    criterio_parada = len(grafo) / (maior_grau + 1)
    ativacao = []
    tamanho_ativacao = 99999999999999

    for subgrafo in subgrafos:
        if verifica_ativacao(subgrafo, grafo):
            if tamanho_ativacao > len(subgrafo):
                ativacao = subgrafo
                tamanho_ativacao = len(subgrafo)

        if tamanho_ativacao == int(criterio_parada):
            return ativacao, tamanho_ativacao

    return ativacao, tamanho_ativacao

if __name__ == '__main__':
    grafo_simples = {
        '1': [['2', '6'], True],
        '2': [['1', '3'], True],
        '3': [['2', '4'], True],
        '4': [['3', '5'], True],
        '5': [['4', '6'], True],
        '6': [['5', '1'], True]
    }

    ativacao, tamanho_ativacao = algoritmo_forca_bruta(grafo_simples)

    print(ativacao)
    print(tamanho_ativacao)
