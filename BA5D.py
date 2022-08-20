# BA5D
# Find the Longest Path in a DAG


def rosalindprint(res):
    return "->".join([str(x) for x in res])


def read_data(file_name):
    with open(file_name) as my_file:
        inlines = [x.strip("\n") for x in my_file.readlines()]
        source = int(inlines[0])
        sink = int(inlines[1])
        edges = {}
        for i in range(2, len(inlines)):
            edge, weight = inlines[i].split(":")
            node1, node2 = edge.split("->")
            if int(node1) in edges.keys():
                edges[int(node1)].append((int(node2), int(weight)))
            else:
                edges[int(node1)] = ([(int(node2), int(weight))])
    return source, sink, edges


def graphForTopOrder(edges):
    graph = {}
    all_nodes = []
    for key in edges.keys():
        for val in edges[key]:
            if key not in graph.keys():
                graph[key] = [val[0]]
            else:
                graph[key].append(val[0])
            if key not in all_nodes:
                all_nodes.append(key)
            if val[0] not in all_nodes:
                all_nodes.append(val[0])
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


def longestPath(edges, source, sink):
    graph, all_nodes = graphForTopOrder(edges)
    n = max(all_nodes)
    s = [0] * (n + 1)
    topOrder = topologicalOredring(graph, all_nodes)
    start = 0
    for i in range(len(topOrder)):
        if topOrder[i] == source:
            start = i
            break
    predecessor = [0] * (n + 1)
    for i in range(start, len(topOrder)):
        t = topOrder[i]
        max_val = 0
        for key in edges.keys():
            for val in edges[key]:
                if val[0] == t and s[key] + val[1] > max_val:
                    s[t] = s[key] + val[1]
                    max_val = s[t]
                    predecessor[t] = key
    pred = predecessor[sink]
    lonPath = [pred, sink]
    while pred != source:
        pred = predecessor[pred]
        lonPath.insert(0, pred)

    return s[sink], lonPath


if __name__ == "__main__":
    #source, sink, edges = read_data("./d.txt")
    source, sink, edges = read_data("./rosalind_ba5d.txt")
    lpLength, lp = longestPath(edges, source, sink)
    print(lpLength)
    print(rosalindprint(lp))
