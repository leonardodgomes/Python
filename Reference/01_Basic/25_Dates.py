# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)


# Date Output ***************************************************************************************************
#  When we execute the code from the example above the result will be:
#  2022-02-28 09:54:55.989148
#  The date contains year, month, day, hour, minute, second, and microsecond.
#  The datetime module has many methods to return information about the date object.


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# Creating Date Objects
#  To create a date, we can use the datetime() class (constructor) of the datetime module.
#  The datetime() class requires three parameters to create a date: year, month, day.
#  The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
#    but they are optional, and has a default value of 0, (None for timezone).

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


# The strftime() Method
#  The datetime object has a method for formatting date objects into readable strings.
#  The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

#Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# A reference of all the legal format codes: ****************************************************************************

# Directive  - Description                                                  -       Example
# %a         - Weekday, short version                                       -       Wed
# %A         - Weekday, full version                                        -       Wednesday
# %w         - Weekday as a number 0-6, 0 is Sunday                         -       3
# %d         - Day of month 01-31                                           -       31
# %b         - Month name, short version                                    -       Dec
# %B         - Month name, full version                                     -       December
# %m         - Month as a number 01-12                                      -       12
# %y         - Year, short version, without century                         -       18
# %Y         - Year, full version                                           -       2018
# %H         - Hour 00-23                                                   -       17
# %I         - Hour 00-12                                                   -       5
# %p         - AM/PM                                                        -       PM
# %M         - Minute 00-59                                                 -       41
# %S         - Second 00-59                                                 -       8
# %f         - Microsecond 000000-999999                                    -       548513
# %z         - UTC offset                                                   -       100
# %Z         - Timezone                                                     -       CST
# %j         - Day number of year 001-366                                   -       365
# %U         - Week number of year, Sunday as the first day of week, 00-53  -       52
# %W         - Week number of year, Monday as the first day of week, 00-53  -       52
# %c         - Local version of date and time                               -       Mon Dec 31 17:41:00 2018
# %C         - Century                                                      -       20
# %x         - Local version of date                                        -       12/31/18
# %X         - Local version of time                                        -       0,736805555555556
# #%%        - A % character                                                -       %
# %G         - ISO 8601 year                                                -       2018
# %u         - ISO 8601 weekday (1-7)                                       -       1
# %V         - ISO 8601 weeknumber (01-53)                                  -       1




# String to Date

import datetime as dt

date_time_str = '2022-12-01'
# strptime(input_string, input_format)
date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%d')

print('Date:', date_time_obj.date())




# String to Date and time

import datetime

date_time_str = '2022-12-01 10:27:03.929149'
# strptime(input_string, input_format)
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)




# String to Datetime with Timezone

import datetime as dt
import pytz

date_time_str = '2022-06-29 17:08:00'
date_time_obj = dt.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

timezone = pytz.timezone('America/New_York')
timezone_date_time_obj = timezone.localize(date_time_obj)

print(timezone_date_time_obj)
print(timezone_date_time_obj.tzinfo)



# Python: Get difference between two dates in years
#   In python, the dateutil module provides a class relativedelta, which represents
#   an interval of time. The relativedelta class has following attributes which tells about the duration,

from datetime import datetime
from dateutil import relativedelta
date_1 = datetime(2021, 7, 2)
date_2 = datetime(2032, 3, 24)
# Get the interval between two dates
diff = relativedelta.relativedelta(date_2, date_1)
print('Difference between dates in years: ', diff.years)
print('Complete Difference between two dates: ')
print(diff.years , ' years, ', diff.months, ' months and ', diff.days, ' days')





# Convert String to Datetime with Maya

import maya

dt = maya.parse('2018-04-29T17:45:25Z').datetime()
print(dt.date())
print(dt.time())
print(dt.tzinfo)