# BA1D
# Pattern Matching Problem
# Find All Occurrences of a Pattern in a String


def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text


def find_starting_positions(Pattern, Genome):
    positions = []
    k = len(Pattern)
    for i in range(0, len(Genome)):
        if Genome[i:i + k] == Pattern:
            positions.append(i)
    return positions


if __name__ == '__main__':
    with open("./rosalind_ba1d.txt", "r") as myfile:
        Pattern = myfile.readline().strip("\n")
        Genome = myfile.readline().strip("\n")
    text_file = open("rosalind_ba1d_output.txt", "w")
    text_file.write(rosalindprint(find_starting_positions(Pattern, Genome)))
    text_file.close()
