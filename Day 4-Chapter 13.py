# Author: Gan Li
# Date: 9/14/21 2:32 下午
# Description:
import string


def word(sentence, new_file):
    low = sentence.lower().strip()
    for i in range(len(low)):
        if low[i] in string.punctuation or low[i] in string.whitespace:
            low = low.replace(low[i], '\n', 1)
    new_file.write(low)
    new_file.write('\n')


if __name__ == "__main__":
    file = open('Tom Sawyer.txt', 'r')
    new = open('new.txt', 'w')
    line = file.readline()
    for line in file:
        word(line, new)
    new.close()
