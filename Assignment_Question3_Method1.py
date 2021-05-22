# 3.Write a Python program to display the current date and time.
# Developed by : Yamini Rathod C0796390
# Date : 16-05-2021

import datetime

print('The program to display the current date and time. Prepared by : Yamini Rathod C0796390')

currenttime = datetime.datetime.now()
#currentday = datetime.datetime.day()
#currentyear = datetime.date.today().year

print('Current Date & Time : {}'.format(currenttime.strftime("%Y/%m/%d %H:%M:%S")))
#print(currentday)
#print(currentyear)