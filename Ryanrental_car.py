#Ryan Mackenzie
#IT140 - Intro to scripting
#Final rental car billing script

import sys
'''
Section 1: Collect customer input
'''

#Variable to store the rental code
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

#Requesting amount of time rented from user for mileage charges
if rentalCode == 'W':
  rentalPeriod = input("Number of Weeks Rented:\n")
else:
  rentalPeriod = input("Number of Days Rented:\n")


#Checks to see which base charge to apply based on the rentalCode
if rentalCode == "B":
  baseCharge = float(rentalPeriod) * 40.00
elif rentalCode == "D":
  baseCharge = float(rentalPeriod) * 60.00
else:
  baseCharge = float(rentalPeriod) * 190.00



#Asks the user for starting and ending miles, then calulates the difference
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart) #these were stored as strings, need to change to ints


#Variable to store the total milage charge
mileCharge = 0

#Calculates milage charge for budget rentals
if rentalCode == "B":
  mileCharge = totalMiles * 0.25

#Calculates milage charge for daily rentals, 
elif rentalCode == "D":
  averageDayMiles = totalMiles / int(rentalPeriod)
  if averageDayMiles > 100:     #Checks to see if a milage charge needs to be applied
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25

#Calculates the milage charge for Weekly rentals.
elif rentalCode == "W":
  averageWeekMiles = totalMiles / int(rentalPeriod)
  if averageWeekMiles > 900:    #Checks to see if a milage charge needs to be applied.
    mileCharge =  rentalPeriod * 100

#Calculates the final rental charge for all types
amtDue = mileCharge + baseCharge


#Prints out the rental summary properly formatted
print("Rental Summary\nRental Code:        " + rentalCode + "\nRental Period:        " + rentalPeriod)
print("Starting Odometer:  " + str(odoStart) + "\nEnding Odometer:    " +  str(odoEnd) + "\nMiles Driven:       " + str(totalMiles))
print('Amount Due:         $%.2f' % (amtDue)) #Formatted to always show two decimals for cents