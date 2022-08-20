# BA1G
# Hamming Distance Problem
# Compute the Hamming Distance Between Two Strings

def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist


if __name__ == "__main__":
    with open("./rosalind_ba1g.txt", "r") as myfile:
        stringA = myfile.readline().strip("\n")
        stringB = myfile.readline().strip("\n")
    print(HammingDistance(stringA, stringB))
