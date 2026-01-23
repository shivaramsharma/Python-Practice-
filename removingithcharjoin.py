#Python Program for Removing i-th Character from a String join


s = "PythonProgramming"
i = 6

res = ''.join(s[j] for j in range(len(s)) if j != i)
print(res)