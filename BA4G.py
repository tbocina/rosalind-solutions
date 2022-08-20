# BA4G
# Implement LeaderboardCyclopeptideSequencing


def rosalindprint(res):
    return "-".join([str(x) for x in res])


def expand(list):
    peps = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    newlist = []
    for x in list:
        for z in peps:
            y = x.copy()
            y.append(z)
            newlist.append(y)
    return newlist


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
    spec = [0]
    for x in range(1, n):
        for i in range(n):
            if i + x >= n:
                y = i + x - n
                spec.append(sum(peptide[i:]) + sum(peptide[:y]))
            else:
                spec.append(sum(peptide[i:i + x]))
    spec.append(sum(peptide))
    spec.sort()
    return spec


def circScore(peptide, spectrum):
    spec = cyclospectrum(peptide)
    score = 0
    for s in spectrum:
        if s in spec:
            spec.remove(s)
            score += 1

    return score


def cut(leaderboard, spectrum, n):
    if len(leaderboard) <= n:
        return leaderboard
    scores = []
    for x in leaderboard:
        scores.append(circScore(x, spectrum))
    scores.sort()
    scores.reverse()
    min = scores[n - 1]
    new = []
    for x in leaderboard:
        if circScore(x, spectrum) >= min:
            new.append(x)
    return new


def leaderboardCyclopeptideSequencing(spectrum, n):
    leaderboard = [[]]
    leaderPeptide = []
    leaderScore = 0
    while leaderboard != []:
        leaderboard = expand(leaderboard)
        newleaderboard = []
        for pep in leaderboard:
            if sum(pep) == spectrum[-1]:
                if circScore(pep, spectrum) >= leaderScore:
                    leaderPeptide = pep
                    leaderScore = circScore(pep, spectrum)
            if sum(pep) <= spectrum[-1]:
                newleaderboard.append(pep)
        leaderboard = cut(newleaderboard, spectrum, n)
    return leaderPeptide


if __name__ == "__main__":
    """
    n = 10
    spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
    print(rosalindprint(leaderboardCyclopeptideSequencing(spectrum, n)))
    """
    with open("./rosalind_ba4g.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        n = int(inlines[0])
        spectrum = [int(x) for x in inlines[1].split()]

    text_file = open("./rosalind_ba4g_output.txt", "w")
    text_file.write(rosalindprint(leaderboardCyclopeptideSequencing(spectrum, n)))
    text_file.close()