# BA4H
# Generate the Convolution of a Spectrum


def rosalindprint(res):
    r = []
    for key, value in res.items():
        for i in range(value):
            r.append(key)
    return " ".join([str(x) for x in r])


def convolution(spectrum):
    n = len(spectrum)
    conv = {}
    for i in range(n):
        for j in range(n):
            diff = spectrum[i] - spectrum[j]
            if diff > 0:
                if diff not in conv.keys():
                    conv[diff] = 1
                else:
                    conv[diff] += 1
    return conv


if __name__ == "__main__":
    """
    spectrum = [0, 137, 186, 323]
    print(rosalindprint(convolution(spectrum)))
    """
    with open("./rosalind_ba4h.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        spectrum = [int(x) for x in inlines[0].split()]

    text_file = open("./rosalind_ba4h_output.txt", "w")
    text_file.write(rosalindprint(convolution(spectrum)))
    text_file.close()