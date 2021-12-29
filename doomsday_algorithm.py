# -*- coding: utf-8 -*-
"""
@Hank - 12/22/2021

My attempt to programmatically re-create the doomsday method for finding the 
day of the week for any date.

"""

# imports
import math

# get the target date from the user
print("Enter a date to learn what day of the week it falls on.")

day = input("Day: ")
month = input("Month: ")
year = input("Year: ")

# cleanup inputs of day and month if they are input as single digits
day = day.zfill(2)
month = month.zfill(2)

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

# find the doomsday of the century
# This converts the century num to day num
century_dict = {0: 2, 1: 0, 2: 5, 3: 3}

# The day num can be found in day_dict
century_factor = century_dict[int(century) % 4]

# find the decade "section" we're in (every 28 years the calendar repeats)
decade_section = int(decade) % 28
leap_year_factor = int(math.floor(decade_section) / 4)
decade_factor = decade_section + leap_year_factor  # sum the decade factor

# determine if year is a leap year
year = int(year)

leap_year = (year % 4 == 0 and year % 100 != 0) or \
    (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)

# leap year corrections for the following month_dict
if leap_year:
    x = 4  # these variables correspond to jan + feb doomsday if no leap year
    y = 29
else:
    x = 3  # these variables correspond to jan + feb doomsday if yes leap year
    y = 28

# find the day num code
doomsday = (century_factor + decade_factor) % 7

# doomsday anchor points corresponding to their months
month_dict = {'01': x, 
              '02': y, 
              '03': 14, 
              '04': 4, 
              '05': 9, 
              '06': 6, 
              '07': 11,
              '08': 8, 
              '09': 5, 
              '10': 10, 
              '11': 7, 
              '12': 12
              }

# day dictionary
day_dict = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']

# find the difference between the user selected day and doomsday
day_diff = int(month_dict[month]) - int(day)
day_diff = day_diff % 7  # ignore day differences that complete a week

# find the day of the week
final_day = (doomsday - day_diff) % 7

# translate the final day to a str and print it out
print(f"\nThis date falls on a {day_dict[final_day]}.")