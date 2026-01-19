#Python program to print even length words in a string
from collections import Counter
string1 = "This is the python programming"

res = string1.split()

for s in res:
    if len(s)%2 == 0:
        print(s)

