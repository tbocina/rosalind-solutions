# BA1C
# Reverse Complement Problem
# Find the Reverse Complement of a String

def ReverseComplement(Pattern):
    elements = list(Pattern)
    result = []
    for el in elements:
        if el == 'A':
            result.append('T')
        elif el == 'T':
            result.append('A')
        elif el == 'C':
            result.append('G')
        else:
            result.append('C')
    result = result[::-1]
    patternReverse = "".join(result)
    return patternReverse


if __name__ == '__main__':
    with open("./rosalind_ba1c.txt", "r") as myfile:
        text = myfile.readline().strip("\n")
    text_file = open("rosalind_ba1c_output.txt", "w")
    text_file.write(ReverseComplement(text))
    text_file.close()
