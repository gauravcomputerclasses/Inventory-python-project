# Write a Python program that takes the **quantities of multiple items requested** and their corresponding **available stock**, and validates if the **entire order can be fulfilled**.

# 📦 Logic:
# - If **all requested quantities** are **less than or equal to** their available stock → Show: "All items in stock — Proceed to checkout."
# - If **any item exceeds** available stock → Show: "Some items are out of stock — Cannot proceed."

item1 = int(input("Enter the Quantity Required By customer for item 1 -> "))
item1Stock = int(input("Enter The Stock Of Item 1 -> "))
item2 = int(input("Enter the Quantity Required By customer for item 2 -> "))
item2Stock = int(input("Enter The Stock Of Item 2 -> "))

if ((item1 <= item1Stock) and (item2 <= item2Stock)):
        print("All items in stock — Proceed to checkout.")

else:
        print("Some items are out of stock — Cannot proceed.")