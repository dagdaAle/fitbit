import csv
from time import sleep
import requests
import json
from datetime import timedelta, date
# This is a python file you need to have in the same directory as your code so you can import it
import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
pd.options.display.max_rows = 999
import datetime

if __name__ == "__getsleep__":
    pass

#function for get all sleep data
def getsleep(start_date , end_date) :
        CLIENT_ID='2389G5'
        CLIENT_SECRET='636c18786967602847f7396da3456f41'

        def daterange(start_date, end_date):
            for n in range(int ((end_date - start_date).days)):
                yield start_date + timedelta(n)

        #autorization proccess
        server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
        server.browser_authorize()
        ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
        auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

        day_count = 0

        date_list = []

        
        for single_date in daterange(start_date, end_date):
            date_list.append(single_date.strftime("%Y-%m-%d"))
            day_count +=1

        

        #-------------------------------------------------------------------------------------------------------------
        #sleep data
        sleep = auth2_client.time_series("sleep",base_date=start_date,end_date=end_date)
        data_dump = json.dumps(sleep['sleep'])
        info = json.loads(data_dump)

        #liste for the values 
        list_awakeCount= []
        list_awakeDuration= []
        list_awakeningsCount= []
        list_dateOfSleep= []
        list_duration = []
        list_efficiency= []
        list_minutesAfterWakeup= []
        list_minutesAsleep = []
        list_minutesAwake= []
        list_minutesToFallAsleep= []
        list_restlessCount= []
        list_restlessDuration= []
        list_timeInBed = []



        for data in info: 
            list_dateOfSleep.append(data['dateOfSleep'])
            list_awakeCount.append(data['awakeCount'])
            list_awakeDuration.append(data['awakeDuration'])
            list_awakeningsCount.append(data['awakeningsCount'])
            list_duration.append(data['duration'])
            list_efficiency.append(data['efficiency'])
            list_minutesAfterWakeup.append(data['minutesAfterWakeup'])
            list_minutesAsleep.append(data['minutesAsleep'])
            list_minutesAwake.append(data['minutesAwake'])
            list_minutesToFallAsleep.append(data['minutesToFallAsleep'])
            list_restlessCount.append(data['restlessCount'])
            list_restlessDuration.append(data['restlessDuration'])
            list_timeInBed.append(data['timeInBed'])

        
        print(list_awakeningsCount)

        #creation of a dictionary for the list
        dict = {'dateOfSleep' : list_dateOfSleep, 'awakeCount' : list_awakeCount, 'awakeDuration' : list_awakeDuration, 'awakeningsCount' : list_awakeningsCount,
                'duration' : list_duration, 'efficiency' : list_efficiency,'minutesAfterWakeup' : list_minutesAfterWakeup,
                'minutesAsleep' : list_minutesAsleep, 'minutesAwake' : list_minutesAwake,'minutesToFallAsleep' : list_minutesToFallAsleep,
                'restlessCount' : list_restlessCount, 'restlessDuration' : list_restlessDuration,'timeInBed' : list_timeInBed}
        df = pd.DataFrame(dict)
        print(df)

        #dictionary to csv
        df.to_csv("source/data/sleep.csv",index=False)

