# BA3B
# Reconstruct a String from its Genome Path


def GetString(genome_path):
    text = genome_path[0]
    for i in range(1, len(genome_path)):
        text += genome_path[i][-1]
    return text


if __name__ == '__main__':
    """
    genome_path=['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']
    print(GetString(genome_path))
    """
    with open("./rosalind_ba3b.txt") as myfile:
        genome_path = [x.strip("\n") for x in myfile.readlines()]
    text_file = open("./rosalind_ba3b_output.txt", "w")
    text_file.write(GetString(genome_path))
    text_file.close()
