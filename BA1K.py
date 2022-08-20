# BA1K
# Generate the Frequency Array of a String


def rosalindprint(res):
    return " ".join([str(x) for x in res])


def patternToNumber(pattern):
    res = 0
    k = 0
    for x in pattern[::-1]:
        if x == "C":
            res = res + 1 * (4 ** k)
        if x == "G":
            res = res + 2 * (4 ** k)
        if x == "T":
            res = res + 3 * (4 ** k)
        k = k + 1
    return res


def computingFrequencies(text, k):
    frequencyArray = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1
    return frequencyArray


if __name__ == "__main__":
    """
    text = "ACGCGGCTCTGAAA"
    k = 2
    print(rosalindprint(computingFrequencies(text, k)))
    """

    with open("./rosalind_ba1k.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    text = inlines[0]
    k = int(inlines[1])

    text_file = open("./rosalind_ba1k_output.txt", "w")
    text_file.write(rosalindprint(computingFrequencies(text, k)))
    text_file.close()
