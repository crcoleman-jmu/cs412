import random
import optimal_solution

def generate_large_graph(size):
    """
    Generate a random larger graph with the given size.
    """
    graph = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            # Add edges with a lower probability to create a sparse graph
            if random.random() < 0.2:
                graph[i][j] = graph[j][i] = 1
    return graph

# Generate a larger graph (e.g., size = 20)
large_graph = generate_large_graph(20)

# Find the maximum clique (this may take a long time)
result = optimal_solution.max_clique_bruteforce(large_graph)
print("Maximum Clique:", result)
