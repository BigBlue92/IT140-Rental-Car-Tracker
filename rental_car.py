import sys
#setting base cost variable to numerical values
baseB = 40.00
baseD = 60.00
baseW = 190.00
#Get input for rental code and assigning string to rentalCode
cInput = str(input("(B)udget, (D)aily, or (W)eekly rental?\n"))
rentalCode = cInput.upper()
#Branching If else statement asking for rentalPeriod and assigning numerical value to rental Period variable
if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n"))
else:
  rentalPeriod = int(input("Number of Days Rented:\n"))
#Branching if, elif, else statement calculating baseCharge and assigning numeric value to variable
if rentalCode == "B":
  baseCharge = rentalPeriod * baseB
elif rentalCode == "D":
  baseCharge = rentalPeriod * baseD
else:
  baseCharge = rentalPeriod * baseW
#User imput assigning numerical value to odoStart
odoStart = int(input("Starting Odometer Reading:\n"))
#User imput assigning numerical value to odoEnd
odoEnd = int(input("Ending Odometer Reading:\n"))
#Calculate totalMiles and assigning Numerical value to totalMiles variable
totalMiles = odoEnd - odoStart
#Branching if else and nested if else statement to calcuate mileCharge and assign numerical value to mileCharge variable
if rentalCode == "B":
    mileCharge = totalMiles * 0.25
elif rentalCode == "D":
    if (totalMiles/rentalPeriod) > 100:
        mileCharge = ((totalMiles/rentalPeriod) - 100) * 0.25
    else:
        mileCharge = 0
else:
    if (totalMiles/rentalPeriod) > 900:
        mileCharge = rentalPeriod * 100
    else:
        mileCharge = 0
#Calculate total amount due and assiging numerical value to amtDue variable
amtDue = baseCharge + mileCharge


print("Rental Code: " + rentalCode)
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: $" + str("%.2f" % float(amtDue)))