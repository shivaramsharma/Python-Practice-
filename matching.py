#Python | Count the Number of matching characters in a pair of string

a = "orange"
b = "apple"

res = len(set(a) & set(b))
print(res)