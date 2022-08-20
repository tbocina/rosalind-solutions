# BA2C
# Profile-most Probable k-mer Problem


def ProfileMost(text, k, profile):
    D = dict()
    for i in range(0, len(text) - k + 1):
        sample = text[i:i + k]
        val = 0
        for j in range(k):
            if sample[j] == 'A':
                val += float(profile[0][j])
            elif sample[j] == 'C':
                val += float(profile[1][j])
            elif sample[j] == 'G':
                val += float(profile[2][j])
            else:
                val += float(profile[3][j])
        D[i] = val
    res = [key for key, value in D.items()
           if value == max(D.values())]
    return text[res[0]:res[0] + k]


if __name__ == '__main__':
    """
    text='ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    k=5
    profile=[[0.2, 0.2, 0.3, 0.2, 0.3],
             [0.4, 0.3, 0.1, 0.5, 0.1],
             [0.3, 0.3, 0.5, 0.2, 0.4],
             [0.1, 0.2, 0.1, 0.1, 0.2]]
    print(ProfileMost(text,k,profile))
    """
    with open("./rosalind_ba2c.txt") as myfile:
        text = myfile.readline().replace("\n", "")
        k = int(myfile.readline())
        L = []
        for i in range(4):
            L.append(myfile.readline().strip().split())
    print(ProfileMost(text, k, L))
