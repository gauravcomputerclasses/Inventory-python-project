# Write a Python program that takes two integers as input and checks whether the first number is divisible by the second number. Print an appropriate message based on the result.

num1 = int(input("Enter a Number -> "))
num2 = int(input("Enter another Number -> "))

if(num1 % num2 == 0):
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")