# BA5E
# Find a Highest-Scoring Alignment of Two Strings


def globalalignment(n, m, down, right, diagonal):
    s = []
    for i in range(n + 1):
        s.append((m + 1) * [0])

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    backtrack = {}
    for i in range(len(down) + 1):
        backtrack[i] = [""] * (len(right[0]) + 1)

    for i in range(1, (len(down) + 1)):
        backtrack[i][0] = "D"
    for j in range(1, len(right[0]) + 1):
        backtrack[0][j] = "R"

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(
                s[i - 1][j] + down[i - 1][j],
                s[i][j - 1] + right[i][j - 1],
                s[i - 1][j - 1] + diagonal[i - 1][j - 1]
            )
            if s[i][j] == s[i - 1][j] + down[i - 1][j]:
                backtrack[i][j] = "D"
            elif s[i][j] == s[i][j - 1] + right[i][j - 1]:
                backtrack[i][j] = "I"
            else:
                backtrack[i][j] = "M"

    return s[n][m], backtrack


def construct_moves(backtrack):
    n = len(backtrack) - 1
    m = len(backtrack[0]) - 1

    moves = []
    while n > 0 or m > 0:
        moves.append(backtrack[n][m])
        if backtrack[n][m] == "D":
            n = n - 1
        elif backtrack[n][m] == "I":
            m = m - 1
        else:
            m = m - 1
            n = n - 1

    return moves[::-1]


def moves_to_strings(first_word, second_word, moves):
    pointer_w1 = 0
    pointer_w2 = 0

    w1 = []
    w2 = []

    for move in moves:
        if move == "D":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append("-")
        if move == "I":
            w1.append("-")
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1
        if move == "M":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1

    return "".join(w1), "".join(w2)


if __name__ == "__main__":
    fp = open("./blosum62.scoring", "r")
    scores = [x.strip("\n") for x in fp.readlines()]
    Scores = {}
    names = scores[0].split()
    for line in scores[1:]:
        tmp = line.split()
        letter = tmp[0]
        scoring = [int(x) for x in tmp[1:]]
        Scores[letter] = {k: v for k, v in zip(names, scoring)}

    """
    first_word = "PLEASANTLY"
    second_word = "MEANLY"
    """

    with open("./rosalind_ba5e.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    first_word, second_word = inlines

    v = [-5] * (len(second_word) + 1)
    down = {k: v for k in range(len(first_word))}

    v = [-5] * len(second_word)
    right = {k: v for k in range(len(first_word) + 1)}

    diagonal = {}
    for idx, l1 in enumerate(first_word):
        row = []
        for l2 in second_word:
            row.append(Scores[l1][l2])
        diagonal[idx] = row

    res, backtrack = globalalignment(
        len(first_word), len(second_word), down, right, diagonal
    )

    moves = construct_moves(backtrack)

    w1, w2 = moves_to_strings(first_word, second_word, moves)

    text_file = open("./rosalind_ba5e_output.txt", "w")
    text_file.writelines([str(res), "\n", w1, "\n", w2])
    text_file.close()