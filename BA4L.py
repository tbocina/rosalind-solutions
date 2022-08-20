# BA4L
# Trim a Peptide Leaderboard


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


def score(peptide, spectrum):
    ls = linearSpectrum(peptide)
    score = 0
    for s in spectrum:
        if s in ls:
            ls.remove(s)
            score += 1

    return score


def trim(leaderboard, spectrum, n):
    import operator
    linearScores = {}
    res = []
    for i in range(len(leaderboard)):
        peptide = leaderboard[i]
        linearScores[leaderboard[i]] = score(peptide, spectrum)
    linearScores = dict(sorted(linearScores.items(), key=operator.itemgetter(1), reverse=True))
    val = 0
    last_val = max(linearScores.values())
    for key, value in linearScores.items():
        if val >= n and value < last_val:
            break
        res.append(key)
        val += 1
        last_val = value
    return res


if __name__ == "__main__":
    """
    leaderboard = ["LAST", "ALST", "TLLT", "TQAS"]
    spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
    n = 2
    print(rosalindprint(trim(leaderboard, spectrum, n)))
    """

    with open("./rosalind_ba4l.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        leaderboard = inlines[0].split()
        spectrum = [int(x) for x in inlines[1].split()]
        n = int(inlines[2])

    text_file = open("./rosalind_ba4l_output.txt", "w")
    text_file.write(rosalindprint(trim(leaderboard, spectrum, n)))
    text_file.close()
