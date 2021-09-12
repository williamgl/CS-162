# Author: Gan Li
# Date: 9/12/21 11:39 上午
# Description: Case study: word play

file = open('words.txt')
line = file.readline()
for line in file:
    if len(line.strip()) > 20:
        print(line.strip())

