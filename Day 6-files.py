# Author: Gan Li
# Date: 10/21/21 11:19 上午
# Description:
import pickle
import json

cat_list = ['Siamese', 'Manx', 'Abyssinian', 'Savannah', 'Jammy']

with open('cats.pkl', 'wb') as infile:
    pickle.dump(cat_list, infile)

rbfile = open('cats.pkl', 'rb')
list_cats = pickle.load(rbfile)
rbfile.close()
for cat in list_cats:
    print(cat.strip())

with open('cats.json', 'w') as jsonfile:
    json.dump(cat_list, jsonfile)

with open('cats.json', 'r') as jsonread:
    catlist = json.load(jsonread)

for cat in catlist:
    print(cat)
