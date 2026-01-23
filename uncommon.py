#Find Uncommon Words from Two Strings - Python

A = "Geeks for Geeks new"
B = "Learning from Geeks for Geeks"

a = set(A.split())
b = set(B.split())

res = print(a ^ b)


