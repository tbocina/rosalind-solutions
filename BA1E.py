# BA1E
# Clump Finding Problem
# Find Patterns Forming Clumps in a String

def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text


def clump_finding(Genome, k, L, t):
    res = []
    for i in range(0, len(Genome) - L + 1):
        for j in range(i, i + L - k):
            if Genome[i:i + L].count(Genome[j:j + k]) == t:
                if Genome[j:j + k] not in res:
                    res.append(Genome[j:j + k])
    return res


if __name__ == '__main__':
    with open("./rosalind_ba1e.txt", "r") as myfile:
        Genome = myfile.readline().strip("\n")
        k, L, t = map(int, myfile.readline().strip().split())
    text_file = open("rosalind_ba1e_output.txt", "w")
    text_file.write(rosalindprint(clump_finding(Genome, k, L, t)))
    text_file.close()
