# BA6C
# Compute the 2-Break Distance Between a Pair of Genomes


def string_to_int_repr(text):
    return [int(x) for x in text.split(" ")]


def rosalind_input(text):
    chromosomes = text.split(")")
    chromosomes = [string_to_int_repr(chrom[1:]) for chrom in chromosomes[:-1]]
    return chromosomes


def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
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


def get_n_cycles(edges):
    edges = edges.copy()
    n_cycles = 0
    starting = edges[0][1]
    del edges[0]
    while True:
        found = False
        for i in range(len(edges)):
            if starting == edges[i][0]:
                starting = edges[i][1]
                found = True
                break
            if starting == edges[i][1]:
                starting = edges[i][0]
                found = True
                break
        if found:
            del edges[i]
        else:
            n_cycles += 1
            if len(edges) == 0:
                break
            starting = edges[0][1]
            del edges[0]

    return n_cycles


if __name__ == "__main__":
    """
    genome_P = "(+1 +2 +3 +4 +5 +6)"
    genome_Q = "(+1 -3 -6 -5)(+2 -4)"
    """

    with open("./rosalind_ba6c.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        genome_P, genome_Q = inlines

    chromosomes_P = rosalind_input(genome_P)
    chromosomes_Q = rosalind_input(genome_Q)

    colored_edges_P = get_colored_edges(chromosomes_P)
    colored_edges_Q = get_colored_edges(chromosomes_Q)

    colored_edges_breakpoint_PQ = colored_edges_P + colored_edges_Q
    n_cycles = get_n_cycles(colored_edges_breakpoint_PQ)

    n_syn_blocks = 0
    for chrom in chromosomes_P:
        n_syn_blocks += len(chrom)

    print(n_syn_blocks - n_cycles)
