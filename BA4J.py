# BA4J
# Generate the Theoretical Spectrum of a Linear Peptide


def rosalindprint(res):
    return " ".join([str(x) for x in res])


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


if __name__ == "__main__":
    """
    peptide = "NQEL"
    print(rosalindprint(linearSpectrum(peptide)))
    """
    with open("./rosalind_ba4j.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    peptide = inlines[0]
    text_file = open("./rosalind_ba4j_output.txt", "w")
    text_file.write(rosalindprint(linearSpectrum(peptide)))
    text_file.close()