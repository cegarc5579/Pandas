## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array(
                [               
                    [150.68,207.99,107.88,58.99,60.59],
                    [20.89,98.99,258.62,19.76,101.59],
                    [70.66,190.10,134.54,200.14,15.59],
                    [10.52,201.59,140.55,13.99,45.98]
                ])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
sumarray = salesArray.sum()
print(sumarray)

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
minimumsale = salesArray.min()
maximumsale = salesArray.max()
print("Smallest sale: ", minimumsale)
print("Biggest sale: ", maximumsale)

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")
flattened = salesArray.flatten()
salesgreat = flattened[flattened >= 100]
print(salesgreat)

## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
registersales = np.sum(salesArray, axis = 1) #axis=1 is by columns
for i in range(len(registersales)):
    print("Register", i+1, "sale:", registersales[i])
print()

## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")
ccfee = 0.02
regfees = [sum(i) * ccfee for i in salesArray]
tfees = [[i*ccfee for i in row]for row in salesArray]
totalfees = np.sum(regfees)
print("Fees for each register are:", regfees)
#print(tfees)
print('The total amount of fees is:', totalfees)

## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")
Profit = salesArray-tfees
print("Sales are:",salesArray)
print("Fees are:",tfees)
print("Profit made on sale:",Profit)

print()

## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")
print(salesArray[[1,3]])
print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")
newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
salesArray = np.vstack((salesArray, newRegister))
print(salesArray)

## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")
salesArray[2,3] = 20.14
print(salesArray)

