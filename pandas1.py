#pd is the common alias for pandas
import pandas as pd

grades = pd.Series([87,100,94])

print(grades)

a = pd.Series(98.6,range(3))

#this is the first element in our array, so 0 = 87
b = grades[0]
c = grades.count()
d = grades.mean()
#the following code gives you everything in one output
print(grades.describe())


grades = pd.Series([87,100,94], index=['Wally', 'Eva','Sam'])
#print(grades)

grades_dict = {'Wally': 87, 'Eva':100, 'Sam':94}

grades_ds = pd.Series(grades_dict)
#the keys become the indexes, and the values stay 
print(grades_ds)

eva = grades['Eva']

wally = grades.Wally

#this gives us a numpy array of just the values 
e = grades.values

#
hardware = pd.Series(['Hammer','Saw','Wrench'])

f = hardware.str.contains('a')
g = hardware.str.upper()

#convert a series object to a Python list
hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])
#this compares where the elements are the same
#returns back true and false for matches 
h = ds1 == ds2

i = ds1 > ds2

j = ds1 < ds2

#convert series of list to one series
#this has 3 different elements
#each element is a list
#3 separate lists
list_of_series = pd.Series([
    ['Red','Green','White'],
    ['Red','Black'],
    ['Yellow']
])
#this is how you make it into one series and reset the indexes as well
list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop = True)

#sort a series

s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values()

#can't sort elements of different data types, all elements have to be the same in order to sort 
#s = pd.Series(['100',200,'python',300.12, '400'])
#sorted_series = s.sort_values()
#the code above will give you an error


#adding to a series

s.append(pd.Series(['500','php']))#you have to reassign it to the original series in order for it to append, 
#follow next line of code to reassing to original series
s = s.append(pd.Series(['500','php'])).reset_index(drop=True)


#write a Pandas program to calculate the frequency counts of each unique
#value of a given series 

import random
list1 = [random.randrange(1,10)for i in range(0,100)]
s = pd.Series(list1)
result = s.value_counts()#shows us each of the count for each of the number we have in our list 







print()