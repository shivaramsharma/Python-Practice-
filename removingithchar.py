#Python Program for Removing i-th Character from a String

Input = "PythonProgramming"
i = 6

output = ""
length = len(Input)
for p in range (0, length):
    if p != i:
        output = output + Input[p]     
    else:
        pass
print(output)

