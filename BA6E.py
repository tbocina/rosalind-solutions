# BA6E
# Find All Shared k-mers of a Pair of Strings


def rosalindprint(res):
    return "\n".join([str(x) for x in res])


def reverse_complement(text):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complement[x] for x in text[::-1]])


def get_all_reverse_complements(k, text):
    rev_compl = []
    for i in range(len(text) - k + 1):
        rev_compl.append((reverse_complement(text[i:i + k]),i))
    return rev_compl


def sharedKMers(k, text1, text2):
    rev_compl1 = get_all_reverse_complements(k, text1)
    rev_compl2 = get_all_reverse_complements(k, text2)
    res = []
    for i in range(len(text1) - k + 1):
        kmer1 = text1[i:i + k]
        for j in range(len(text2) - k + 1):
            kmer2 = text2[j:j + k]
            if kmer1 == kmer2:
                res.append((i, j))
        for rc in rev_compl2:
            if kmer1 == rc:
                res.append((i, rc[1]))
    for rc in rev_compl1:
        for j in range(len(text2) - k + 1):
            kmer2 = text2[j:j + k]
            if rc[0] == kmer2:
                res.append((rc[1], j))
    return res


if __name__ == "__main__":
    """
    k = 3
    text1 = "AAACTCATC"
    text2 = "TTTCAAATC"
    print(rosalindprint(sharedKMers(k, text1, text2)))
    """

    with open("./rosalind_ba6e.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        k = int(inlines[0])
        text1 = inlines[1]
        text2 = inlines[2]
    res = sharedKMers(k, text1, text2)

    text_file = open("./rosalind_ba6e_output.txt", "w")
    text_file.write(rosalindprint(res))
    text_file.close()
