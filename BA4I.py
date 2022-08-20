# BA4I
# Implement ConvolutionCyclopeptideSequencing


def rosalindprint(res):
    return "-".join([str(x) for x in res])


def convolution(spectrum):
    n = len(spectrum)
    conv = {}
    for i in range(n):
        for j in range(n):
            diff = spectrum[i] - spectrum[j]
            if diff > 0:
                if diff not in conv.keys():
                    conv[diff] = 1
                else:
                    conv[diff] += 1
    res = []
    for key, value in conv.items():
        for i in range(value):
            res.append(key)
    return res


def convolution_restricted(spectrum, m):
    import operator
    convres = []
    conv = convolution(spectrum)
    d = {}
    for i in range(len(conv)):
        if 57 <= conv[i] <= 200:
            if conv[i] not in d.keys():
                d[conv[i]] = 1
            else:
                d[conv[i]] += 1
    d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    val = 0
    last_val = max(d.values())
    for key, value in d.items():
        if val >= m and value < last_val:
            break
        convres.append(key)
        val += 1
        last_val = value
    return convres


def expand(list, peps):
    # peps = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    newlist = []
    for x in list:
        for z in peps:
            y = x.copy()
            y.append(z)
            newlist.append(y)
    return newlist


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


def leaderboardCyclopeptideSequencing(spectrum, n, conv):
    leaderboard = [[]]
    leaderPeptide = []
    leaderScore = 0
    while leaderboard != []:
        leaderboard = expand(leaderboard, conv)
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
    m = 20
    n = 60
    spectrum = [57, 57, 71, 99, 129, 137, 170, 186, 194, 208, 228, 265, 285, 299, 307, 323, 356, 364, 394, 422, 493]
    conv = convolution_restricted(spectrum, m)
    leaderPeptide = leaderboardCyclopeptideSequencing(spectrum, n, conv)
    print(conv)
    print(rosalindprint(leaderPeptide))
    """
    with open("./rosalind_ba4i.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        m = int(inlines[0])
        n = int(inlines[1])
        spectrum = [int(x) for x in inlines[2].split()]
    conv = convolution_restricted(spectrum, m)
    leaderPeptide = leaderboardCyclopeptideSequencing(spectrum, n, conv)
    print(rosalindprint(leaderPeptide))