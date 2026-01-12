#- Reverse a string without using slicing ([::-1]).

a = "shivaram"
print(a)
p = ""
l = len(a)-1
for t in range(l,-1,-1):
    p = p + a[t]
print(p)