# BA6A
# Implement GreedySorting to Sort a Permutation by Reversals


def greedy_sorting(str_permutation):
    helper = [int(x) for x in str_permutation[1:-1].split()]

    S = []

    for i in range(len(helper)):
        if helper[i] == i + 1:
            continue

        idx = i
        while True:
            if helper[idx] == i + 1 or helper[idx] == -1 * (i + 1):
                break
            idx += 1

        mid = [-1 * x for x in helper[i:(idx + 1)]][::-1]
        helper = helper[0:i] + mid + helper[(idx + 1):]
        S.append(helper.copy())

        if helper[i] < 0:
            helper[i] = abs(helper[i])
            S.append(helper.copy())

    return S


def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"


def rosalind_print(permutations):
    strings = []
    for perm in permutations:
        strings.append("(" + " ".join([f(x) for x in perm]) + ")")
    return "\n".join(strings)


if __name__ == "__main__":
    """
    str_permutation = "(-3 +4 +1 +5 -2)"
    res = greedy_sorting(str_permutation)
    print(rosalind_print(res))
    """

    with open("./rosalind_ba6a.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
    str_permutation = inlines[0]
    res = greedy_sorting(str_permutation)

    text_file = open("./rosalind_ba6a_output.txt", "w")
    text_file.write(rosalind_print(res))
    text_file.close()
