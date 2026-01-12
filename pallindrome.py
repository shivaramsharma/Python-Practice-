#Write a function to check if a string is a palindrome.

number = "556655"
number1 = number[::-1]

print(number1)

if(number == number1):
    print("given number is pallindrome")
else:
    print("given number is not a pallindrome")