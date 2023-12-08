def is_clique(graph, nodes):
    """
    Check if the given set of nodes forms a clique in the graph.
    """
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not graph[nodes[i]][nodes[j]]:
                return False
    return True

def max_clique_bruteforce(graph):
    """
    Brute-force approach to find the maximum clique in the graph.
    """
    max_clique = []

    # Iterate through all possible combinations of nodes
    for i in range(1, 2**len(graph)):
        nodes = [j for j, bit in enumerate(bin(i)[:1:-1]) if bit == '1']
        
        # Check if the current set of nodes forms a clique and is larger than the current max_clique
        if is_clique(graph, nodes) and len(nodes) > len(max_clique):
            max_clique = nodes

    return max_clique



def main():

    m = int(input())

    edge_list = [input().split() for _ in range(m)]
    graph = {}

    for edge in edge_list:

        u, v = edge

        graph.setdefault(u, set()).add(v)

        graph.setdefault(v, set()).add(u)


    max_clique_output = max_clique_bruteforce(graph)

    print(max_clique_output)


if __name__ == "__main__":

    main()


# Example usage

