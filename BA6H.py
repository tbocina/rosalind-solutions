# BA6H
# Implement ColoredEdges


def string_to_int_repr(text):
    return [int(x) for x in text.split(" ")]


def rosalind_input(text):
    chromosomes = text.split(")")
    chromosomes = [string_to_int_repr(chrom[1:]) for chrom in chromosomes[:-1]]
    return chromosomes


def chromosome_to_cycle(permutation):
    cycle = []
    for x in permutation:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def get_colored_edges(chromosomes):
    edges = []
    for chrom in chromosomes:
        nodes = chromosome_to_cycle(chrom)
        for j in range(1, len(nodes) - 1, 2):
            edges.append((nodes[j], nodes[j + 1]))
        edges.append((nodes[-1], nodes[0]))
    return edges


def rosalind_print(edges):
    return repr(edges)[1:-1]


if __name__ == "__main__":
    """
    text = "(+1 -2 -3)(+4 +5 -6)"
    chromosomes = rosalind_input(text)
    print(rosalind_print(get_colored_edges(chromosomes)))
    """

    with open("./rosalind_ba6h.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    text = inlines[0]
    chromosomes = rosalind_input(text)

    text_file = open("./rosalind_ba6h_output.txt", "w")
    text_file.write(rosalind_print(get_colored_edges(chromosomes)))
    text_file.close()
