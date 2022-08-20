# BA1N
# Generate the d-Neighborhood of a String


def rosalindprint(res):
    return "\n".join([x for x in res])


def HammingDistance(p, q):
    # computes the hamming distance between strings p and q
    if len(p) != len(q):
        return -1
    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1
    return dist


def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffixNeighbors = neighbors(pattern[1:], d)
    for sn in suffixNeighbors:
        if HammingDistance(pattern[1:], sn) < d:
            for i in ['A', 'C', 'G', 'T']:
                neighborhood.append(i + sn)
        else:
            neighborhood.append(pattern[0] + sn)
    return neighborhood


if __name__ == "__main__":
    """
    pattern = "ACG"
    d = 1
    print(rosalindprint(neighbors(pattern, d)))
    """

    with open("./rosalind_ba1n.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    pattern = inlines[0]
    d = int(inlines[1])

    text_file = open("./rosalind_ba1n_output.txt", "w")
    text_file.write(rosalindprint(neighbors(pattern, d)))
    text_file.close()
