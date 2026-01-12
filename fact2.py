def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1  # Base case
    else:
        return n * factorial_recursive(n - 1) # Recursive step

number = 6
print(f"The factorial of {number} is {factorial_recursive(number)}")