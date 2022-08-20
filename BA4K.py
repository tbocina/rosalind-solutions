# BA4K
# Linear Peptide Scoring Problem


def get_amino_acid_mass():
    mass = {
        "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
        "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
        "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
        "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
    }

    return mass


def prefixMass(peptide):
    mass = get_amino_acid_mass()
    prefMass = [0]
    m = 0
    for pep in peptide:
        m += mass[pep]
        prefMass.append(m)
    return prefMass


def linearSpectrum(peptide):
    LinearSpectrum = [0]
    prefMass = prefixMass(peptide)
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            LinearSpectrum.append(prefMass[j] - prefMass[i])
    return sorted(LinearSpectrum)


def score(peptide, spectrum):
    ls = linearSpectrum(peptide)
    score = 0
    for s in spectrum:
        if s in ls:
            ls.remove(s)
            score += 1

    return score


if __name__ == "__main__":
    """
    peptide = "NQEL"
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    print(score(peptide, spectrum))
    """

    with open("./rosalind_ba4k.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        peptide = inlines[0]
        spectrum = [int(x) for x in inlines[1].split()]

    print(score(peptide, spectrum))