# BA5G
# Compute the Edit Distance Between Two Strings


def editDist(s1, s2):
    n = len(s1)
    m = len(s2)
    x = [[0 for x in range(m + 1)] for y in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0 or j == 0:
                x[i][j] = max(i, j)
            else:
                x[i][j] = min(
                    x[i - 1][j] + 1,
                    x[i][j - 1] + 1,
                    x[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)
                )
    return x[n][m]


if __name__ == "__main__":
    """
    s1 = "PLEASANTLY"
    s2 = "MEANLY"
    print(editDist(s1, s2))
    """
    with open("./rosalind_ba5g.txt") as myfile:
        inlines=[x.strip("\n") for x in myfile.readlines()]
    s1, s2 = inlines
    print(editDist(s1, s2))
