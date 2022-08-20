# BA1H
# Approximate Pattern Matching Problem
# Find All Approximate Occurrences of a Pattern in a String

def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text.strip()


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = text[i : (i + k)]
        try:
            D[tmp].append(i)
        except KeyError:
            D[tmp] = [i]
    return D


def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist


def ApproximatePatternMatching(text, pattern, d):
    """Find All Approximate Occurrences of a Pattern in a String"""
    D = kmersfrequency(text, len(pattern))
    L = list()
    [L.extend(value) for key, value in D.items() if HammingDistance(key, pattern) <= d]
    return sorted(L)


if __name__ == "__main__":

    with open("./rosalind_ba1h.txt", "r") as myfile:
        pattern = myfile.readline().replace("\n", "")
        text = myfile.readline().replace("\n", "")
        d = myfile.readline().replace("\n", "")

    d = int(d)

    text_file = open("./rosalind_ba1h_output.txt", "w")
    text_file.write(rosalindprint(ApproximatePatternMatching(text, pattern, d)))
    text_file.close()
