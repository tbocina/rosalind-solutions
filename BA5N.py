# BA5N
# Find a Topological Ordering of a DAG


def rosalindprint(res):
    return ", ".join([str(x) for x in res])


def rosalindInput(file_name):
    graph = {}
    all_nodes = []
    with open(file_name) as my_file:
        inlines = [x.strip("\n") for x in my_file.readlines()]
    for i in range(len(inlines)):
        source, nodes = inlines[i].split(" -> ")
        source = int(source)
        nodes = [int(x) for x in nodes.split(',')]
        graph[source] = nodes
        if source not in all_nodes:
            all_nodes.append(source)
        for node in nodes:
            if node not in all_nodes:
                all_nodes.append(node)
    return graph, all_nodes


def candidatesList(graph):
    candidates = []
    for node in graph.keys():
        counter = 0
        for node2 in graph.keys():
            if node in graph[node2]:
                counter += 1
        if counter == 0:
            candidates.append(node)
    return candidates


def topologicalOredring(graph, all_nodes):
    List = []
    candidates = candidatesList(graph)
    while candidates != []:
        for i in range(len(candidates)):
            List.append(candidates[i])
        for c in candidates:
            graph.pop(c)
            all_nodes.remove(c)
        candidates = candidatesList(graph)

    for one in sorted(all_nodes):
        List.append(one)

    return List


if __name__ == "__main__":
    """
    graph, all_nodes = rosalindInput("./n.txt")
    print(rosalindprint(topologicalOredring(graph, all_nodes)))
    """
    graph, all_nodes = rosalindInput("./rosalind_ba5n.txt")
    res = topologicalOredring(graph, all_nodes)

    text_file = open("./rosalind_ba5n_output.txt", "w")
    text_file.write(rosalindprint(res))
    text_file.close()