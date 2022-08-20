# construct the De Bruijn Graph of a string

def rosalindprint(D):
    out = ""
    keys = sorted(D.keys())
    for first in keys:
        second = ",".join(sorted(D[first]))
        out = out + f"{first} -> {second}\n"
    return out


def deBrujinGraph(k, text):
    D = {}
    for i in range(0, len(text) - k + 1):
        first = text[i: (i + k - 1)]
        second = text[(i + 1): (i + k)]
        if first not in D:
            D[first] = [second]
        else:
            D[first].append(second)
    return D


if __name__ == '__main__':
    """
    k = 4
    text = "AAGATTCTCTAC"
    r = deBruijnGraph(k, text)
    for key in sorted(r.keys()):
        print(key + ' -> ' + r[key])
    """
    with open("./rosalind_ba3d.txt") as myfile:
        inlines = [x.strip() for x in myfile.readlines()]
        k = int(inlines[0])
        text = inlines[1]
    text_file = open("./rosalind_ba3d_output.txt", "w")
    text_file.write(rosalindprint(deBrujinGraph(k, text)))
    text_file.close()
