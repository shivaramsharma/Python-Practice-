#Given a number, check if it is an integer or a float
x = 10.2
if isinstance(x,int):
    print("x is integer")
elif isinstance(x,float):
    print("x is float")