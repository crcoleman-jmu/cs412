def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i] not in graph or nodes[j] not in graph[nodes[i]]:
                return False
    return True

def find_max_clique(graph, current_clique, remaining_nodes):
    if not remaining_nodes:
        return current_clique

    max_clique = current_clique
    for node in remaining_nodes:
        if all(node in graph[clique_node] for clique_node in current_clique):
            new_clique = find_max_clique(graph, current_clique + [node], [n for n in remaining_nodes if n != node])
            if len(new_clique) > len(max_clique):
                max_clique = new_clique

    return max_clique


def main():
    m = int(input())
    edge_list = [input().split() for _ in range(m)]
    
    # Build the graph
    graph = {}
    for edge in edge_list:
        u, v = edge
        graph.setdefault(u, {}).setdefault(v, True)
        graph.setdefault(v, {}).setdefault(u, True)

    max_clique = find_max_clique(graph, [], list(graph.keys()))

    print(" ".join(max_clique))

if __name__ == "__main__":
    main()
