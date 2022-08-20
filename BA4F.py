# BA4F
# Compute the Score of a Cyclic Peptide Against a Spectrum


def get_amino_acid_mass():
    mass = {
        "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
        "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
        "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
        "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
    }

    return mass


def theoretical_spectrum(peptide):
    n = len(peptide)
    mass = get_amino_acid_mass()

    extended_peptide = peptide + peptide[:-1]

    spectrum = []
    spectrum.append(0)
    spectrum.append(sum([mass[x] for x in peptide]))

    for l in range(n):
        for k in range(1, n):
            subpeptide = extended_peptide[l:l + k]
            spectrum.append(sum([mass[x] for x in subpeptide]))

    return sorted(spectrum)


def score(peptide, spectrum):
    ts = theoretical_spectrum(peptide)
    score = 0
    for s in spectrum:
        if s in ts:
            ts.remove(s)
            score += 1

    return score


if __name__ == "__main__":
    """
    peptide = "NQEL"
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    print(score(peptide, spectrum))
    """

    with open("./rosalind_ba4f.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        peptide = inlines[0]
        spectrum = [int(x) for x in inlines[1].split()]

    print(score(peptide, spectrum))