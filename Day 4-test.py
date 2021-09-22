# Author: Gan Li
# Date: 9/14/21 3:49 下午
# Description:
file = open('new.txt')
line = file.readline()
i = 0
dic = {}
for line in file:
    dic[line] = 0
print(len(dic))
file.close()
