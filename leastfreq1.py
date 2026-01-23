from collections import Counter

s = "GeeksforGeeks"

freq = Counter(s)
print(freq)

res = min(freq,key=freq.get)

print(str(res))

