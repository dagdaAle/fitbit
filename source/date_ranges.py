import csv
from numpy import kaiser
import requests
import json
from datetime import timedelta, date
# This is a python file you need to have in the same directory as your code so you can import it
import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
pd.options.display.max_rows = 999
import datetime


import pandas as pd
from datetime import datetime

import datetime

if __name__ == "__generateDateRange__":
    pass

def generateDateRange(start,end):
    my_start = str(start)
    my_end = str(end)
    start_date = datetime.datetime.strptime(my_start, "%Y-%m-%d").strftime('%Y-%m-%d')
    end_date = datetime.datetime.strptime(my_end,"%Y-%m-%d").strftime('%Y-%m-%d')
    #generate all the date between start and end
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

    #print(date_generated)
    list_days = []

    for date in date_generated:
        my = datetime.datetime.strptime(str(date),"%Y-%m-%d").strftime('%Y-%m-%d')
        list_days.append(date.strftime("%Y-%m-%d"))

    

    date_ranges = []
    i = 0
    
    #save the the date in an intervall of 100 days
    for i in range(0,len(list_days)) :

        if  len(list_days) < 100:
            date_ranges.append(start)
            date_ranges.append(end)
            break
        if i % 100 == 0:
            date_ranges.append(list_days[i])
            i += 100
        if i+100 > len(list_days): 
            date_ranges.append(list_days[i])
            date_ranges.append(list_days[-1])
            print(list_days[i])
            break
    
    #the format for the API has to be Y-m-d

    return date_ranges


start_date = datetime.datetime(2011,2,3).date()
end_date = datetime.datetime(2020,6,3).date()
my_list = generateDateRange(start_date,end_date)
print(my_list)

