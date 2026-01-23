#Using Regular Expressions
import re

s = 1010001000001111

if re.fullmatch('[01]+', s):
    print("yes")
else:
    print("No")