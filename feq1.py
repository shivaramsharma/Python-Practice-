#ython - Words Frequency in String Shorthands

from collections import Counter

s = "hello world hello everyone"

res = Counter(s.split())

print(res)