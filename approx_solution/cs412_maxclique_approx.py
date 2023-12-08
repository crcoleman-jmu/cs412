"""
Title:  Max Clique Approximation
Authors: Chase Coleman & Nicholas St.Amour
Date: 12/7/23
"""


def bron_kerbosch(graph, r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return

    for vertex in list(p):
        bron_kerbosch(graph, r.union([vertex]), p.intersection(graph[vertex]), x.intersection(graph[vertex]), cliques)
        p.remove(vertex)
        x.add(vertex)

def find_max_clique(graph):
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    max_clique = max(cliques, key=len)
    sorted_clique = sorted(max_clique)
    return ' '.join(sorted_clique)


def main():
    m = int(input())
    edge_list = [input().split() for _ in range(m)]
    
    graph = {}
    for edge in edge_list:
        u, v = edge
        graph.setdefault(u, set()).add(v)
        graph.setdefault(v, set()).add(u)

    max_clique_output = find_max_clique(graph)
    
    print(max_clique_output)

if __name__ == "__main__":
    main()
