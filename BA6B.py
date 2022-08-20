# BA6B
# Compute the Number of Breakpoints in a Permutation


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return [0] + tmp + [len(tmp) + 1]


def is_adjacency(pair):
    if pair[1] - pair[0] == 1:
        return True
    return False


def n_adjacencies(permutation):
    count = 0
    for i in range(len(permutation) - 1):
        count += is_adjacency((permutation[i], permutation[i + 1]))
    return count


def n_breakpoints(permutation):
    return len(permutation) - 1 - n_adjacencies(permutation)


if __name__ == "__main__":
    """
    text = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
    permutation = rosalind_input(text)
    print(n_breakpoints(permutation))
    """

    with open("./rosalind_ba6b.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    text = inlines[0]
    permutation = rosalind_input(text)
    print(n_breakpoints(permutation))
