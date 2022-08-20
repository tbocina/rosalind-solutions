# BA3M
# Generate All Maximal Non-Branching Paths in a Graph


def rosalindInputToGraph(edges):
    D = {}
    all_nodes = []
    for edge in edges:
        first, second = edge.split(" -> ")
        first = int(first)
        second = [int(x) for x in second.split(",")]
        D[first] = second
        if first not in all_nodes:
            all_nodes.append(first)
        for s in second:
            if s not in all_nodes:
                all_nodes.append(s)
    return D, all_nodes


def isOneinOneOut(graph, node):
    if node in graph.keys():
        in_nodes = 0
        for key, value in graph.items():
            for val in value:
                if val == node:
                    in_nodes += 1
        if in_nodes == 1 and len(graph[node]) == 1:
            return True
    return False


def maximalNonBranchingPaths(graph, all_nodes):
    paths = []
    for node in graph.keys():
        if not isOneinOneOut(graph, node):
            for v in graph[node]:
                nonBranchingPath = [(node, v)]
                if node in all_nodes:
                    all_nodes.remove(node)
                if v in all_nodes:
                    all_nodes.remove(v)
                while isOneinOneOut(graph, v):
                    nonBranchingPath.append((v, graph[v][0]))
                    v = graph[v][0]
                    if v in all_nodes:
                        all_nodes.remove(v)
                paths.append(nonBranchingPath)

    for node in all_nodes:
        cycle = []
        if isOneinOneOut(graph, node):
            used = [node]
            v = graph[node][0]
            if v in all_nodes and isOneinOneOut(graph, v):
                cycle.append((node, v))
            while v in all_nodes and isOneinOneOut(graph, v):
                if v in used and v != node:
                    break
                used.append(v)
                cycle.append((v, graph[v][0]))
                v = graph[v][0]
                if v == node:
                    for el in cycle:
                        if el[0] in all_nodes:
                            all_nodes.remove(el[0])
                        if el[1] in all_nodes:
                            all_nodes.remove(el[1])
                    break
        paths.append(cycle)
    return paths


def rosalindoutput(paths):
    res = ""
    for path in paths:
        res += str(path[0][0])
        for p in path:
            res += " -> " + str(p[1])
        res += "\n"
    return res


if __name__ == "__main__":
    # edges = ["1 -> 2", "2 -> 3", "3 -> 4,5", "6 -> 7", "7 -> 6"]

    with open("./rosalind_ba3m.txt") as myfile:
        edges = [x.strip("\n") for x in myfile.readlines()]

    graph, all_nodes = rosalindInputToGraph(edges)
    paths = maximalNonBranchingPaths(graph, all_nodes)
    # print(rosalindoutput(paths))

    text_file = open("rosalind_ba3m_output.txt", "w")
    text_file.write(rosalindoutput(paths))
    text_file.close()
