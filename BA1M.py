# BA1M
# Implement NumberToPattern
# Convert an integer to its corresponding DNA string

def NumberToPattern(index, k):
    pattern = list()
    D = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    q = index
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern.append(D[r])
    return "".join(pattern[::-1])


if __name__ == '__main__':
    with open("./rosalind_ba1m.txt", "r") as myfile:
        index = int(myfile.readline())
        k = int(myfile.readline())
    print(NumberToPattern(index, k))
