# BA5C
# Find a Longest Common Subsequence of Two Strings


def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res = s1[i - 1] + res
            i -= 1
            j -= 1
    return res


if __name__ == "__main__":
    """
    s1 = 'AACCTTGG'
    s2 = 'ACACTGTGA'
    print(lcs(s1, s2))
    """
    with open("./rosalind_ba5c.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    s1 = inlines[0]
    s2 = inlines[1]

    text_file = open("./rosalind_ba5c_output.txt", "w")
    text_file.write(lcs(s1, s2))
    text_file.close()