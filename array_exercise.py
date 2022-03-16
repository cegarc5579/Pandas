## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
array23 = np.full((4,3), 2)
print(array23)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

array45 = np.arange(0,120,10).reshape(3,4)
print(array45) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
array2 = np.arange(0,120,10).reshape(4,3)
print(array2)

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
array34 = array2 * 3
print(array34)

## Step 5: Multiply your array from step one by your array from step 2
#print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")
#array9 = array23 * array45
## This errored out... why?
#print(array9)
#this errored out because they are not the same format/same shape

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
array00 = array23 * array2
## this worked! why?
print(array00)
#this works  because they are the same structure and can be multiplied together 



