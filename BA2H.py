# BA2H
# Implement DistanceBetweenPatternAndStrings

import math


def HammingDistance(p, q):
    # computes the hamming distance between strings p and q
    if len(p) != len(q):
        return -1
    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1
    return dist


def DistancePatternString(pattern, dna_list):
    k = len(pattern)
    distance = 0
    for text in dna_list:
        hammDist = math.inf
        for i in range(0, len(text) - k + 1):
            kmer = text[i:(i + k)]
            if HammingDistance(pattern, kmer) < hammDist:
                hammDist = HammingDistance(pattern, kmer)
        distance += hammDist
    return distance


if __name__ == '__main__':
    """
    pattern = 'AAA'
    dna_list = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
    print(DistancePatternString(pattern, dna_list))
    """
    with open("./rosalind_ba2h.txt", "r") as myfile:
        inlines = [x.strip("\n").split(" ") for x in myfile.readlines()]
        pattern = inlines[0][0]
        dna_list = inlines[1:][0]
    print(DistancePatternString(pattern, dna_list))
