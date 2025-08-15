print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponent\n")

userChoice = input("User Choice dalo => ")
if (int(userChoice) in [1,2,3,4,5]):
    num1 = float(input("Enter the first number -> "))
    num2 = float(input("Enter the second number -> "))
else:
    print("Invalid choice, please try again.")

if (userChoice == "1"):
    print("Addition:", num1 + num2)
elif (userChoice == "2"):
    print("Subtraction:", num1 - num2)
elif (userChoice == "3"):
    print("Multiplication:", num1 * num2)
elif (userChoice == "4"):
        print("Division:", num1 / num2)
elif (userChoice == "5"):
    print("Exponent:", num1 ** num2)
else:
    print("Invalid choice, please try again.")
