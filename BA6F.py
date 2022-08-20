# BA6F
# Implement ChromosomeToCycle


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return tmp


def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def rosalind_print(cycle):
    return "(" + " ".join([str(x) for x in cycle]) + ")"


if __name__ == "__main__":
    """
    text = "(+1 -2 -3 +4)"
    chromosome=rosalind_input(text)
    print(rosalind_print(chromosome_to_cycle(chromosome)))
    """

    with open("./rosalind_ba6f.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    text = inlines[0]
    chromosome = rosalind_input(text)

    text_file = open("./rosalind_ba6f_output.txt", "w")
    text_file.write(rosalind_print(chromosome_to_cycle(chromosome)))
    text_file.close()
