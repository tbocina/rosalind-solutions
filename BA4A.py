# BA4A
# Protein Translation Problem:
# Translate an RNA string into an amino acid string

def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text.strip()


def codon():
    d = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R',
         'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H',
         'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R',
         'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
         'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
         'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '*', 'UAC': 'Y', 'UAG': '*', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S',
         'UCG': 'S', 'UCU': 'S', 'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L',
         'UUU': 'F'}
    return d


def translation(rna_pattern):
    G = codon()
    res = []
    for i in range(0, len(rna_pattern), 3):
        letter = G[rna_pattern[i:i + 3]]
        if letter == '*':
            break
        res.append(letter)
    res = "".join(res)
    return res


if __name__ == "__main__":
    """
    rna_pattern = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    peptide = translation(rna_pattern)
    print(peptide)
    """
    with open("./rosalind_ba4a.txt", "r") as myfile:
        text = myfile.readline().replace("\n", "")

    text_file = open("rosalind_ba4a_output.txt", "w")
    text_file.write(rosalindprint(translation(text)))
    text_file.close()