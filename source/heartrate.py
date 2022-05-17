import csv
from csv import reader
import datetime
from email import header
from hashlib import new
from imp import new_module
from itertools import count
import mysqlx
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

import csv
import requests
import json
from datetime import timedelta, date
# This is a python file you need to have in the same directory as your code so you can import it
import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
pd.options.display.max_rows = 999
import datetime





if __name__ == "__getheartrate__":
    pass

def getheartrate(start_date , end_date) :
    CLIENT_ID='2389G5'
    CLIENT_SECRET='636c18786967602847f7396da3456f41'
    count = 0

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)
            count = count + 1

    server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
    auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

    heart = auth2_client.time_series("activities/heart",base_date=start_date,end_date=end_date)
    #print(heart)

    
    data = json.dumps(heart["activities-heart"])

    new_data = json.loads(data)

    

    for n in range(int ((end_date - start_date).days)):
        count = count + 1

    f = open('source\data\heart.csv', 'w',  newline='')
    writer = csv.writer(f)
    header = ['dateTime','caloriesOut',"max","min",'minutes',"name","restingHeartRate"]
    writer.writerow(header)

    for i in range(count) : 
        for k in range(4) :
            my_data = new_data[i]
            row = []
            row.append(my_data["dateTime"])
            if 'caloriesOut' not in my_data["value"]["heartRateZones"][k]:
                row.append("0")
            else:
                row.append(my_data["value"]["heartRateZones"][k]["caloriesOut"])

            row.append(my_data["value"]["heartRateZones"][k]["max"])
            row.append(my_data["value"]["heartRateZones"][k]["min"])

            if 'minutes' not in my_data["value"]["heartRateZones"][k] :
                row.append("0")
            else:
                row.append(my_data["value"]["heartRateZones"][k]["minutes"])
            row.append(my_data["value"]["heartRateZones"][k]["name"])
            if 'restingHeartRate' not in my_data["value"] :
                 row.append("0")
            else:
                row.append(my_data["value"]["restingHeartRate"])
            writer.writerow(row)
        
    f.close()

#--------------------------------------------------------------------------------------------

#getheartrate(start_date , end_date)