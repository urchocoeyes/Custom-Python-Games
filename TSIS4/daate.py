'''
    Write a Python program to subtract five days from current date.
'''
import datetime
today = datetime.datetime.now()
today_minus_5 = datetime.datetime(today.year, today.month, today.day - 5, today.hour, today.minute, today.second, today.microsecond)
print(today_minus_5)

import datetime
time_now = datetime.datetime.now()
time_5_days_ago = time_now - datetime.timedelta(days = 5)
print(time_5_days_ago)

time_5_days_ago = datetime.timedelta(days = 5) # --> 5 days, 0:00:00

'''
    Write a Python program to print yesterday, today, tomorrow.
'''
from datetime import *
yesterday = datetime.now() - timedelta(days = 1)
print("yesterday: ", yesterday)
today = datetime.now()
print("today: ",today)
tomorrow = today + timedelta(days = 1)
print("tomorrow: ",tomorrow)

from datetime import *
today = datetime.now()
for i in range(-1,2):  # -1: yesterday, 0: today, 1: tomorrow
    result = today.day + i
    print(f"for {i}th day from {today}, today: ", result)
    
import datetime 
now = datetime.datetime.now()
yesterday = now + datetime.timedelta(days = -1)
tomorrow = now + datetime.timedelta(days = 1)
print("Now:", now, now.strftime('%A'), sep="  ")
print("Yesterday:", yesterday, yesterday.strftime('%A'), sep="  ")
print("Tomorrow:", tomorrow, tomorrow.strftime('%A'), sep="  ")

    
'''
    Write a Python program to drop microseconds from datetime.
'''
import datetime
time_now = datetime.datetime.now()
time_now = time_now.replace(microsecond = 0)
print(time_now) # 2023-03-06 13:15:38

import datetime 
time_now = datetime.datetime.now()
drop = time_now.strftime('%c')
print(drop) # Mon Mar  6 07:23:09 2023

'''
    Write a Python program to calculate two date difference in seconds.
'''
from datetime import *
date1 = datetime(2005, 7, 11, 0, 0, 18)
print(date1.strftime('%c')) # 07/11/05 00:00:18
date2 = datetime(2005, 7, 11, 0, 0, 14)
print(date2.strftime("%c")) # 07/11/05 00:00:14
diff = date1 - date2 # 0:00:04
print(diff)

#2nd option
import datetime
date_1 = datetime.datetime(*list(map(int, input("Year, month, day, hour, minutes, seconds: ").split())))
date_2 = datetime.datetime(*list(map(int, input("Year, month, day, hour, minutes, seconds: ").split())))
difference = abs(date_1 - date_2)
print("Difference between 2 dates in seconds:", difference.days * 24 * 3600 + difference.seconds,"seconds")