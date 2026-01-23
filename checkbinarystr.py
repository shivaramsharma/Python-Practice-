#Check if a given string is binary string or not - Python
'''
a = "111110"

b = set(a)

c ={'1','0'}

if( b == c):
    print("given string is binary")
else:
    print("given string is not binary")
'''

s = "01010000111"

if set(s).issubset({'0','1'}):
    print("given string is binary")
else:
    print("given string is not binary")

