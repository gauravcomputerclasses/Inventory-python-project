units = int(input("Enter Number of units -> "))
fixedCharge = 200
billAmmount = 0

# units till 0-150
if (units > 0 and units <= 150):
    billAmmount = (units*4.50) + fixedCharge
# 
elif(units>150 and units<=250):
    billAmmount = (units-150)*6.50 + (150*4.50) + fixedCharge

else:
    billAmmount = (150*4.50) + (100*6.50) + (units-250)*7.20  + fixedCharge
    
    
print(f"You consumed {units} wnits your total bill is\n{billAmmount}")