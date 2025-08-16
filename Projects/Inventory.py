userChoice = "y"
stock = {
    "apples": 25,
    "bananas": 40,
    "oranges": 18,
}
allItems = stock.keys()

def displayMenu():
    print()
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
        exitProgram()
    else:
        return "Invalid Choice"
    
def addItem():
    itemName = input("Enter Item Name -> ").lower()
    itemQty = int(input("Enter Quantity -> "))
    
    if (itemName in allItems):
        currentQty = stock.get(itemName) #25
        stock.update({itemName:currentQty+itemQty}) #35
        print(stock) # return
        
    else:
        stock[itemName] = itemQty
        print(stock) # return
     
def removeItem():
    itemName = input("Enter Item Name -> ").lower()
    
    if (itemName in allItems):
        stock.pop(itemName)
        finalResult(f"{itemName} removed successfully")
    else:
        finalResult("Item Not Found")    
    
def displyItems():
    if (stock == {}):
        finalResult("\nNo items in the inventory")
    else:
        print(f"{'Item':<15}{'Quantity':<10}")
        print("-" * 25)
        for i in allItems:
              print(f"{i:<15}{stock.get(i):<10}") 
    
def updateItems():
    itemName = input("Enter Item Name -> ").lower()
    if (itemName in allItems):
        print("Item Found\n")
        itemQty = int(input("Enter Updated Quantity "))
        stock[itemName] = itemQty
        finalResult("Updated\n")
    else:
        finalResult("Item Not Found") 
        
def searchItem():
    itemName = input("Enter Item Name -> ").lower()
    if (itemName in allItems):
        print(f"{itemName:<15}{stock.get(itemName):<10}")
    else:
        finalResult("Item Not Found") 

def exitProgram():
    global userChoice
    userChoice = "n"

def finalResult(value):
    print(value)

# MAIN PROGRAM

while (userChoice.lower() == "y"):
    displayMenu()
    if (userInput()=="Invalid Choice") : break