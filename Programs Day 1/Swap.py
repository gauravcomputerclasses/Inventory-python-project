a = int(input("Enter Value of a "))
b = int(input("Enter Value of b "))

print(f"The original value of a was {a} and b was {b}")

a = a + b
b = a - b
a = a - b

print(f"Value after swapping for a is {a} and b is {b}")