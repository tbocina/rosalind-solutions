# BA4E
# Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum


def rosalindprint(res):
    return " ".join(sorted(["-".join([str(y) for y in x]) for x in res]))


def get_amino_acid_mass():
    mass = {
        "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
        "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
        "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
        "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
    }

    return mass


def cyclospectrum(peptide):
    n = len(peptide)
    mass = get_amino_acid_mass()

    extended_peptide = peptide + peptide[:-1]

    spectrum = [0, sum(peptide)]

    for l in range(n):
        for k in range(1, n):
            subpeptide = extended_peptide[l:l + k]
            spectrum.append(sum(subpeptide))

    return sorted(spectrum)


def linearspectrum(peptide):
    n = len(peptide)
    mass = get_amino_acid_mass()

    spectrum = [0]

    for l in range(n):
        for k in range(1, n - l + 1):
            subpeptide = peptide[l:l + k]
            spectrum.append(sum(subpeptide))

    return sorted(spectrum)


def belongs_spectrum(candidate_spectrum, main_spectrum):
    from collections import Counter

    counter_c_spectrum = Counter(candidate_spectrum)
    counter_m_spectrum = Counter(main_spectrum)

    for key, count in counter_c_spectrum.items():
        if key not in counter_m_spectrum:
            return False
        if count > counter_m_spectrum[key]:
            return False
    return True


def check_cyclo(spectrum, peptide):
    parent_mass = max(spectrum)

    if sum(peptide) == parent_mass and cyclospectrum(peptide) == spectrum:
        return True

    return False


def check_linear(spectrum, peptide):
    parent_mass = max(spectrum)

    if sum(peptide) <= parent_mass and belongs_spectrum(
            linearspectrum(peptide), spectrum):
        return True

    return False


def branch_and_bound(spectrum):
    all_combinations = []
    aa_masses = set(get_amino_acid_mass().values())

    parent_mass = max(spectrum)
    peptides = [[]]

    while True:
        candidates = [
            peptide + [aa_mass] for aa_mass in aa_masses for peptide in peptides
        ]
        selected = [
            peptide for peptide in candidates if check_linear(spectrum, peptide)
        ]
        all_combinations.extend(
            [peptide for peptide in selected if check_cyclo(spectrum, peptide)]
        )

        peptides = [peptide for peptide in selected if sum(peptide) != parent_mass]

        if len(peptides) == 0:
            break

    return all_combinations


if __name__ == "__main__":
    """
    peptide=[0, 113, 128, 186, 241, 299, 314, 427]
    print(rosalindprint(branch_and_bound(peptide)))
    """
    with open("./rosalind_ba4e.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        peptide = [int(x) for x in inlines[0].split()]

    text_file = open("./rosalind_ba4e_output.txt", "w")
    text_file.write(rosalindprint(branch_and_bound(peptide)))
    text_file.close()