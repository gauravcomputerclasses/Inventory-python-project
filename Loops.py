n = int(input("Enter the number "))
temp = n
d = 0
while (n > 0):
    digit = n % 10
    d = d*10 + digit
    n //= 10

print("Original Num =>",temp)
print("Reversed Num =>",d)