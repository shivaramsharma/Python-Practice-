#- Write a program that prints the Fibonacci sequence up to n terms.

a,b = 0,1
print(a)
print(b)
for n in range(0,20):
    c = a + b
    print(c)
    a = b
    b = c