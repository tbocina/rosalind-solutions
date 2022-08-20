# BA1F
# Minimum Skew Problem
# Find a Position in a Genome Minimizing the Skew

def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text


def minSkew(Pattern):
    elements = list(Pattern)
    skew = [0]
    res = []
    for i in range(len(elements)):
        if elements[i] == 'C':
            skew.append(skew[-1] - 1)
        elif elements[i] == 'G':
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])
    mini = min(skew)
    for i in range(len(skew)):
        if skew[i] == mini:
            res.append(i)
    return res


if __name__ == '__main__':
    with open("./rosalind_ba1f.txt", "r") as myfile:
        Pattern = myfile.readline().strip("\n")
    print(rosalindprint(minSkew(Pattern)))
