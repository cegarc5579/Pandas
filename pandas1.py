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
print()