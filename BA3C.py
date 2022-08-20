# BA3C
# Construct the Overlap Graph of a Collection of k-mers


def overlapgraph(patterns):
    n = len(patterns)
    d = {}
    for i in range(n):
        for j in range(n):
            if i != j and patterns[i][1:] == patterns[j][:-1]:
                d[patterns[i]] = patterns[j]
    return d


if __name__ == '__main__':
    """
    patterns=['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']
    print(overlapgraph(patterns))
    """
    with open("./rosalind_ba3c.txt") as myfile:
        patterns = [x.strip("\n") for x in myfile.readlines()]
    text_file = open("./rosalind_ba3c_output.txt", "w")
    for key, value in overlapgraph(patterns).items():
        text_file.write(key + ' -> ' + value + '\n')
    text_file.close()
