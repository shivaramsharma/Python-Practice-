#Python Program to Accept the Strings Which Contains all Vowels

string1 = "education"
v = "aeiou"

a = set()

for p in string1:
    if p in v:
        a.add(p)
    if len(a) == 5:
        print(True)
        break

else:
    print(False)