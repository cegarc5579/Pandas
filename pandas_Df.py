#Series = one dimensional array
#DataFrame = two "  "
#each column in a data frame is a series 


import pandas as pd 

grades_dict = {'Wally':[87,96,70],'Eva': [100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]
                }

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

eva = grades['Eva']#this object is 

sam = grades.Sam

#using the loc and iloc methods

test2 = grades.loc['Test2']#loc is short for location
#loc is a zero-base index
#loc uses the custom indexes

test1 = grades.iloc[0]
#iloc uses the actual number

#for consecutive rows
#we just need a colon 
# : = consecutive rows and you don't need a list 
# , = non-consecutive rows and you have to give it a list []

#consecutive
test1_thru_test3 = grades.loc['Test1':'Test3']
#non-consecutive rows
test1_and_test3 = grades.loc[['Test1','Test3']]

test1_and_test2 = grades.iloc[0:2]#iloc method does not include the upper index so you would have to go above and type 2

#view only Eva's and Katie's grades for Test 1 and Test 2

eva_kate_test1_test2 = grades.loc['Test1':'Test2', ['Eva','Katie']]

#view only Sam's THRU Bob's grades for Test 1 and Test 3

sam_thru_bob_test1_test3 = grades.loc[['Test1','Test3'], 'Sam':'Bob']


#boolean indexing
#select everyone with an A grade
grades_A  = grades[grades >=90]

#create a dataframe for everyone with a B grade
grades_B = grades[(grades >= 80) & (grades <90)]


#create a dataframe for everyone with a A or B grade

grades_A_or_B = grades[(grades >=90) | (grades >= 80)]

pd.set_option("precision", 2)
# by student 
print(grades.describe())#gives us all the information about the data set right away 
#by test 
print(grades.T.describe())

#Exercie - get the average of all the students grades on each test 
print(grades.T.mean())

#sort rows by their indices(Test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column names (student names)
# axis = 1 indiciates to sort by column indices
#axis = 0 indicates to sort by row indices 
c_sorted_grades_i = grades.sort_index(axis=1)

#in reverse sort order
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)


print()