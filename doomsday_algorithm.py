# -*- coding: utf-8 -*-
"""
@Hank - 12/22/2021

My attempt to programmatically re-create the doomsday method for finding the 
day of the week for any date.

"""
# imports
import math

# get the target date from the user
date = input('Enter a date to learn the day of the week it falls on: '
            '\n(please format as DD. MM. YYYY.)\n')

date_list = date.split() # split the user input into components

# this block assigns each component a name moving forward
year = date_list[-1] 
month = date_list[-2]
day = date_list[-3]

# split the year into century and decade components
year_list = list(year)

if len(year_list) == 4:
    century = year_list[0] + year_list[1]
    decade = year_list[-2] + year_list[-1]
elif len(year_list) == 3:
    century = year_list[0]
    decade = year_list[-2] + year_list[-1]
else:
    century = 0

# find the day we start the calculation from based on the century
century_dict = {0:2, 1:0, 2:5, 3:3} # This converts the century num to day num
century_factor = century_dict[int(century) % 4]

# determine if year is a leap year
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = "yes"
        else:
            leap_year = "no"
    else:
        leap_year = "yes"
else:
    leap_year = "no"

# find the decade "section" we're in (every 28 years the calendar repeats)
decade_section = int(decade) % 28
leap_year_factor = math.floor(int(decade_section) / 4)
decade_factor = decade_section + leap_year_factor # sum the decade factor

# find the day num code
day_factor = (century_factor + decade_factor) % 7

# day dictionary 
day_dict = {0:'Sunday',
            1:'Monday',
            2:'Tuesday',
            3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday'}

# covert day num code to doomsday
doomsday = day_dict[int(day_factor) % 7]

# leap year corrections for the following month_dict
if leap_year == "no":
    x = 3
    y = 28
else:
    x = 4
    y = 29
    
# doomsday anchor points corresponding to their months
month_dict = {'01':x,
              '02':y,
              '03':14,
              '04':4,
              '05':9,
              '06':6,
              '07':11,
              '08':8,
              '09':5,
              '10':10,
              '11':7,
              '12':12
              }
    
print(month_dict[month])

#print(century)
#print(century_factor)
#print(decade_factor)
#print(day_factor)

# tell the user what century, and therefor what position we start from
#print(f"The date chosen falls in the {century}")

# these are changes made to the file to see how git handles them