# BA2E
# Implement GreedyMotifSearch with Pseudocounts


def rosalindprint(res, newline=False):
    text=""
    sep=" "
    if newline:
        sep="\n"
    for i in res:
        text=text+str(i)+sep
    return text.strip()

def ProbableKmer(string, matrix):
    probable = 1
    for i in range(len(string)):
        if string[i] == 'A':
            probable *= matrix[0][i]
        if string[i] == 'C':
            probable *= matrix[1][i]
        if string[i] == 'G':
            probable *= matrix[2][i]
        if string[i] == 'T':
            probable *= matrix[3][i]
    return probable

# Profile-most probable k-mer in the i-th string in Dna
def FindProfileMostProbableKmer(string, k, matrix):
    seq = dict()
    for i in range(len(string) - k + 1):
        seq[string[i:i + k]] = ProbableKmer(string[i:i + k], matrix)
    res = [key for key, value in seq.items()
           if value == max(seq.values())]
    return res[0]

# Score(Motifs)
def Score(Motifs):
    score = 0
    for i in range(len(Motifs[0])):
        j = [motif[i] for motif in Motifs]
        score += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))
    return score


def GreedyMotifPseudocountsSearch(Dna, k, t):
    # BestMotifs ← motif matrix formed by first k-mers in each string from Dna
    BestMotifs = [dna[:k] for dna in Dna]
    # for each k-mer Motif in the first string from Dna
    for k_mer in [Dna[0][i:i + k] for i in range(len(Dna[0]) - k + 1)]:
        # Motif1 ← Motif
        Motifs = [k_mer]
        # for i = 2 to t
        for i in range(1, t):
            # form Profile from motifs Motif1, …, Motifi - 1
            motifs = Motifs[:i]
            # Motifi ← Profile-most probable k-mer in the i-th string in Dna
            matrix = []
            for nar in ["A", "C", "G", "T"]:
                mat = []
                for j in range(k):
                    mm = [m[j] for m in motifs]
                    mat.append(mm.count(nar) + 1 / (len(motifs)*2))
                matrix.append(mat)
            # Motifs ← (Motif1, …, Motift)
            Motifs.append(FindProfileMostProbableKmer(Dna[i], k, matrix))
        # if Score(Motifs) < Score(BestMotifs), BestMotifs ← Motifs
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


if __name__ == '__main__':
    """
    k, t = 3, 5
    Dna = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC',
           'CACGTCAATCAC', 'CAATAATATTCG']
    print('Best Motifs: ',GreedyMotifSearch(Dna,k,t))
    """
    with open("./rosalind_ba2e.txt", "r") as myfile:
        k, t = map(int, myfile.readline().strip().split())
        Dna = []
        for i in range(t):
            Dna.append(myfile.readline())
    text_file = open("rosalind_ba2e_output.txt", "w")
    text_file.write(rosalindprint(GreedyMotifPseudocountsSearch(Dna, k, t)))
    text_file.close()