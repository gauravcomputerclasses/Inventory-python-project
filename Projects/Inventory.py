userChoice = "y"
def displayMenu():
    menuItems = ["1. Add item","2. Remove item","3. Display inventory","4. Update item quantity","5. Search for an item","6. Exit"]
    for item in menuItems : print(item)

def userInput():
    print()
    operation = int(input("Enter Your Choice -> "))
    
    if operation == 1:
        addItem()
    elif operation == 2:
        removeItem()
    elif operation == 3:
        displyItems()
    elif operation == 4:
        updateItems()
    elif operation == 5:
        searchItem()
    elif operation == 6:
        exit()
    else:
        return "Invalid Choice"
    
def addItem():None
def removeItem():None
def displyItems():None
def updateItems():None
def searchItem():None
def exit():None
def finalResult():None

# MAIN PROGRAM

while (userChoice.lower() == "y"):
    displayMenu()
    if (userInput()=="Invalid Choice") : break
    finalResult()
    userChoice = input("Perform More Operations ? [y/n]")