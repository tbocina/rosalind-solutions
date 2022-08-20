# BA1B
# Frequent Words Problem
# Find the Most Frequent Words in a String

def rosalindprint(res):
    text = ""
    for i in res:
        text = text + " " + str(i)
    return text.strip()

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i: (i + k)]


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return D


def mostfrequentkmer(text, k):
    D = kmersfrequency(text, k)
    maxcount = max(D.values())
    return sorted([x[0] for x in D.items() if x[1] == maxcount])


if __name__ == '__main__':
    with open("./rosalind_ba1b.txt", "r") as myfile:
        text = myfile.readline()
        k = int(myfile.readline())
    text_file = open("rosalind_ba1b_output.txt", "w")
    text_file.write(rosalindprint(mostfrequentkmer(text, k)))
    text_file.close()
