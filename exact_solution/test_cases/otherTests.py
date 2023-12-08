

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

result = max_clique_bruteforce(graph)
print("Maximum Clique:", result)


larger_graph = [
    [0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0]
]

result2 = max_clique_bruteforce(larger_graph)
print("Maximum Clique:", result2)