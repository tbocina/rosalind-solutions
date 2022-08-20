# BA3L
# Construct a String Spelled by a Gapped Genome Path


def GetString(genome_path):
    text = genome_path[0]
    for i in range(1, len(genome_path)):
        text += genome_path[i][-1]
    return text


def rosalindinput(gappedPatterns):
    firstPatterns = []
    secondPatterns = []
    for gp in gappedPatterns:
        firstAndSecond = [x for x in gp.split("|")]
        firstPatterns.append(firstAndSecond[0])
        secondPatterns.append(firstAndSecond[1])
    return firstPatterns, secondPatterns


def stringSpelledByGappedPatterns(k, d, gappedPatterns):
    firstPatterns, secondPatterns = rosalindinput(gappedPatterns)
    prefixString = GetString(firstPatterns)
    suffixString = GetString(secondPatterns)
    for i in range(k + d + 1, len(prefixString)):
        if prefixString[i] != suffixString[i - k - d]:
            return ""
    return prefixString + suffixString[len(suffixString) - (k + d):]


if __name__ == "__main__":
    """
    k, d = 4, 2
    gappedPatterns = ["GACC|GCGC", "ACCG|CGCC", "CCGA|GCCG", "CGAG|CCGG", "GAGC|CGGA"]
    print(stringSpelledByGappedPatterns(k, d, gappedPatterns))
    """

    with open("./rosalind_ba3l.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    k, d = [int(x) for x in inlines[0].split()]
    gappedPatterns = inlines[1:]

    text_file = open("rosalind_ba3l_output.txt", "w")
    text_file.write(stringSpelledByGappedPatterns(k, d, gappedPatterns))
    text_file.close()
