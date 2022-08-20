# BA3H
# Reconstruct a String from its k-mer Composition

def rosalindInputToGraph(reads):
    from collections import defaultdict

    D = defaultdict(lambda: [])

    for read in reads:
        prefix = read[:-1]
        suffix = read[1:]
        D[prefix].append(suffix)

    return D


# will change graph since it is a dict!
def getACycle(graph, possible_starts):
    origin = None
    for start in possible_starts:
        if start in graph:
            origin = start
            break
    if origin is None:
        raise
    cycle = []
    first = origin
    while True:
        if first in graph:
            second = graph[first][0]
            cycle.append([first, second])
            if len(graph[first]) == 1:
                graph.pop(first, None)
            else:
                graph[first] = graph[first][1:]
            if second == origin:
                break
            else:
                first = second
        else:
            break
    return cycle


def start_index(cycle, start):
    s_index = -1
    for i in range(0, len(cycle)):
        if cycle[i][0] == start:
            s_index = i
            break
    return s_index


def eulerianCycle(graph):
    graph = graph.copy()

    cycles = []
    # get all cycles
    possible_starts = list(graph.keys())[:1]
    while len(graph) > 0:
        new_cycle = getACycle(graph, possible_starts)
        possible_starts.extend([x[0] for x in new_cycle])
        possible_starts = list(set(possible_starts))
        cycles.append(new_cycle)

    if len(cycles) == 1:
        path = cycles[0]
    else:
        path = cycles[0]
        for i in range(1, len(cycles)):
            next_ = cycles[i]
            s_index = start_index(path, next_[0][0])
            path = path[:s_index] + next_ + path[s_index:]

    firsts = [x[0] for x in path]
    res = "->".join(firsts) + f"->{path[-1][1]}"

    return res


def RebalanceGraphFromEulearianPathToCycle(graph):
    from collections import Counter

    graph = graph.copy()

    outbalance = {first: len(graph[first]) for first in graph.keys()}

    new_list = []
    for v in graph.values():
        new_list.extend(v)
    inbalance = Counter(new_list)

    all_nodes = set(list(outbalance.keys()) + list(inbalance.keys()))

    for node in all_nodes:
        balance = outbalance.get(node, 0) - inbalance.get(node, 0)
        if balance == 1:
            second = node
        if balance == -1:
            first = node

    graph[first].append(second)

    return graph, first, second


if __name__ == "__main__":
    import re

    """
    k = 4
    reads = ['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC']
    """
    with open("./rosalind_ba3h.txt") as myfile:
        inlines = [x.strip() for x in myfile.readlines()]
        k = int(inlines[0])
        reads = inlines[1:]

    graph = rosalindInputToGraph(reads)
    graph, first, second = RebalanceGraphFromEulearianPathToCycle(graph)

    cycle = eulerianCycle(graph)
    parts = cycle.split(f"{first}->{second}", maxsplit=1)
    if parts[0] == "":
        path = parts[1]
    elif parts[1] == "":
        path = parts[0]
    else:
        part1 = parts[0] + first
        part1_trimmed = part1.split("->", maxsplit=1)[1]
        part2 = second + parts[1]
        path = part2 + "->" + part1_trimmed
    res = re.sub("->.{" + str(k - 2) + "}", "", path)

    text_file = open("./rosalind_ba3h_output.txt", "w")
    text_file.write(res)
    text_file.close()
