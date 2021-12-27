# -*- coding: utf-8 -*-
"""
@Hank - 12/22/2021

My attempt to programmatically re-create the doomsday method for finding the 
day of the week for any date.

"""
# get the target date from the user
date = input('Enter a date to learn the day of the week it falls on: '
            '\n(please format as DD. MM. YYYY.)\n')

date_list = date.split() # split the user input into components

# this block assigns each component a name moving forward
year = date_list[-1] 
month = date_list[-2]
day = date_list[-3]

# split the year into century and decade components
year = list(year)
if len(year) == 4:
    century = year[0] + year[1]
    decade = year[-2] + year[-1]
elif len(year) == 3:
    century = year[0]
    decade = year[-2] + year[-1]
else:
    century = 0

# find the day we start the calculation from based on the century
century_dict = {0:'Tuesday', 1:'Sunday', 2:'Friday', 3:'Wednesday'}
century_day = century_dict[int(century)%4]

# tell the user what century, and therefor what position we start from
print(f"The date chosen falls in the year {year} ")

# these are changes made to the file to see how git handles them