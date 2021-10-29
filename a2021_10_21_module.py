# Author: Gan Li
# Date: 10/21/21 11:20 上午
# Description: Module 5
cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Jammy']

file = open('cats.txt', 'r')

with open('cats.txt', 'w') as outfile:
    for cat in cat_list:
        outfile.write(cat + '\n')

with file:
    for i in range(4):
        file.readline()
    text = file.readline()
    print(text)
    # for line in file:
    #     print(line.strip())
