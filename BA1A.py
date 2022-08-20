# BA1A
# Counting words
# We define Count(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text.

def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


if __name__ == '__main__':
    with open("./rosalind_ba1a.txt", "r") as myfile:
        text = myfile.readline().replace("\n", "")
        pattern = myfile.readline().replace("\n", "")
    print(patterncount(text, pattern))
