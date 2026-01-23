#Using re.split() and '-'.join()  Split and Join a String in Python

import re

a = "Hello, how are you?"

b = re.split(r'\s+', a)
c = "_".join(b)
print(b)
print(c)