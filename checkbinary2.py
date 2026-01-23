#Check if a given string is binary string or not - Python
s = "1010100001211"

if  all(c in '01' for c in s):
    print("yes")
else:
    print("no")