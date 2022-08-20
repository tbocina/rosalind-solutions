# BA6G
# Implement CycleToChromosome


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return tmp


def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
    return chromosome


def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"


def rosalind_print(cycle):
    return "(" + " ".join([f(x) for x in cycle]) + ")"


if __name__ == "__main__":
    """
    text = "(1 2 4 3 6 5 7 8)"
    cycle = rosalind_input(text)
    print(rosalind_print(cycle_to_chromosome(cycle)))
    """

    with open("./rosalind_ba6g.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        text = inlines[0]

    cycle = rosalind_input(text)

    text_file = open("./rosalind_ba6g_output.txt", "w")
    text_file.write(rosalind_print(cycle_to_chromosome(cycle)))
    text_file.close()
