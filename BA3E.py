# construct the De Bruijn graph of a collection of k-mers

def rosalindprint(D):
    out = ""
    keys = sorted(D.keys())
    for first in keys:
        out = out + f"{first} -> {D[first]}\n"
    return out


def debruijn(patterns):
    result = {}
    for i in patterns:
        if i[:-1] not in result.keys():
            result[i[:-1]] = i[1:]
        else:
            result[i[:-1]] += "," + i[1:]
    return result


if __name__ == '__main__':
    """
    patterns = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
    print(rosalindprint(debruijn(patterns)))
    """
    with open("./rosalind_ba3e.txt") as myfile:
        patterns = [x.strip() for x in myfile.readlines()]
    text_file = open("./rosalind_ba3e_output.txt", "w")
    text_file.write(rosalindprint(debruijn(patterns)))
    text_file.close()
