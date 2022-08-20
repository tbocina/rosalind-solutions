# BA2G
# Implement GibbsSampler

import random


def rosalind_print(result, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in result:
        text = text + str(i) + sep
    return text.strip()


def get_kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i: (i + k)]


def get_kmers(text, k):
    """Find indices of all k-mers in text"""
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(get_kmer(text, i, k))
    return kmers


def pattern_prob(pattern, profile):
    """return the probability of observing the pattern with the profile matrix"""
    prob = 1
    for index, letter in enumerate(pattern):
        prob *= profile[letter][index]
    return prob


def profile_most_probable(text, k, profile):
    """
    Find a Profile-most probable k-mer in a string text.
    Profile matrix is represented as a dict.
    """
    max_kmer = ""
    max_p = -1
    kmers = get_kmers(text, k)
    for kmer in kmers:
        tmp = pattern_prob(kmer, profile)
        if tmp > max_p:
            max_kmer = kmer
            max_p = tmp
    return max_kmer


def get_motifs(dna_list, profile):
    k = len(profile["A"])

    motifs = [profile_most_probable(dna_string, k, profile) for dna_string in dna_list]
    return motifs


def create_profile_matrix(pattern_list, pseudo_counts=False):
    """
    Returs a profile matrix as a dict based on a the list patternlist
    """

    k = len(pattern_list[0])

    profile_matrix = {}
    profile_matrix["A"] = [0] * k
    profile_matrix["C"] = [0] * k
    profile_matrix["G"] = [0] * k
    profile_matrix["T"] = [0] * k

    for pattern in pattern_list:
        for index, letter in enumerate(pattern):
            profile_matrix[letter][index] = profile_matrix[letter][index] + 1

    if pseudo_counts:
        profile_matrix["A"] = [x + 1 for x in profile_matrix["A"]]
        profile_matrix["C"] = [x + 1 for x in profile_matrix["C"]]
        profile_matrix["G"] = [x + 1 for x in profile_matrix["G"]]
        profile_matrix["T"] = [x + 1 for x in profile_matrix["T"]]

    for i in range(0, k):
        total = (
                profile_matrix["A"][i]
                + profile_matrix["C"][i]
                + profile_matrix["G"][i]
                + profile_matrix["T"][i]
        )
        profile_matrix["A"][i] = profile_matrix["A"][i] / total
        profile_matrix["C"][i] = profile_matrix["C"][i] / total
        profile_matrix["G"][i] = profile_matrix["G"][i] / total
        profile_matrix["T"][i] = profile_matrix["T"][i] / total
    return profile_matrix


def score(motifs):
    """
    Score discrepancy in motifs
    """
    zzip = zip(*motifs)

    max_count = []
    for x in zzip:
        n_a = sum([y == "A" for y in x])
        n_c = sum([y == "C" for y in x])
        n_g = sum([y == "G" for y in x])
        n_t = sum([y == "T" for y in x])
        max_count.append(len(motifs) - max(n_a, n_c, n_g, n_t))

    return sum(max_count)


def randomized_motif_search_atom(dna_list, k):
    n_dna = len(dna_list[0])

    randpos = [random.randint(0, n_dna - k) for dna in dna_list]
    bestmotifs = [dna[index: (index + k)] for index, dna in zip(randpos, dna_list)]
    motifs = bestmotifs

    while True:
        profile = create_profile_matrix(motifs, pseudo_counts=True)
        motifs = get_motifs(dna_list, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs


def profile_randomly_generated_kmer(text, profile, k):
    import random

    L = []

    for i in range(0, len(text) - k + 1):
        L.append(pattern_prob(text[i: i + k], profile))

    C = sum(L)
    L = [x / C for x in L]

    r = random.uniform(0, 1)
    s = 0
    for ind, x in enumerate(L):
        s = s + x
        if r < s:
            return text[ind: ind + k]


def gibbs_sampler_atom(dna_list, k, N=1000):
    import random

    t = len(dna_list)

    bestmotifs = randomized_motif_search_atom(dna_list, k)
    motifs = list(bestmotifs)

    for j in range(1, N):
        i = random.randint(0, t - 1)

        tmp = list(motifs)
        tmp.pop(i)
        profile = create_profile_matrix(tmp, pseudo_counts=True)

        motifs[i] = profile_randomly_generated_kmer(dna_list[i], profile, k)

        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
    return bestmotifs


def gibbs_sampler(dna_list, k, repeats=20, N=1000):
    bestmotifs = gibbs_sampler_atom(dna_list, k, N)
    for i in range(1, repeats):
        motifs = gibbs_sampler_atom(dna_list, k, N)
        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
    return bestmotifs


if __name__ == '__main__':
    """
    k, t, N = 8, 5, 100
    dna_list = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    print(rosalind_print(gibbs_sampler(dna_list,k,100)))
    """
    with open("./rosalind_ba2g.txt", "r") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        k, t, N = [int(x) for x in inlines[0].strip().split(" ")]
        dna_list = inlines[1:]
    text_file = open("rosalind_ba2g_output.txt", "w")
    text_file.write(rosalind_print(gibbs_sampler(dna_list, k, 100, 1000), True))
    text_file.close()