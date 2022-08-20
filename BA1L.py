# BA1L
# Implement PatternToNumber
# Convert a DNA string to a number

def PatternToNumber(pattern):
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


if __name__ == "__main__":
    with open("./rosalind_ba1l.txt", "r") as myfile:
        pattern = myfile.readline().replace("\n", "")
    print(PatternToNumber(pattern))
