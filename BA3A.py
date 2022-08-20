# BA3A
# Generate the k-mer Composition of a String

def rosalindprint(res, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in res:
        text = text + str(i) + sep
    return text.strip()


def CompositionK(k, text):
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(text[i: (i + k)])
    return sorted(kmers)


if __name__ == '__main__':
    """
    k = 5
    text = 'CAATCCAAC'
    print(rosalindprint(CompositionK(k, text)))
    """
    with open("./rosalind_ba3a.txt") as myfile:
        k = int(myfile.readline())
        text = myfile.readline().strip("\n")
    text_file = open("rosalind_ba3a_output.txt", "w")
    text_file.write(rosalindprint(CompositionK(k, text),True))
    text_file.close()
