import cs412_maxclique_exact

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

result = cs412_maxclique_exact.max_clique_bruteforce(graph)
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

result2 = cs412_maxclique_exact.max_clique_bruteforce(larger_graph)
print("Maximum Clique:", result2)