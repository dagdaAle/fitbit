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


if __name__ == "__getactivity__":
    pass

#function for get all activity data
def getactivity(start_date , end_date) :
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

    #-------------------------------------------------------------------------------------------------------------

    #count for the date-range
    day_count = 0

    date_list = []

    #crate a list with all the data and update the count
    for single_date in daterange(start_date, end_date):
        date_list.append(single_date.strftime("%Y-%m-%d"))
        day_count +=1

    #-------------------------------------------------------------------------------------------------------------
    #1 : activityCalories
    activities_calories = auth2_client.time_series("activities/activityCalories",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-activityCalories'])
    info = json.loads(data_dump)

    #add the data to a list
    list_activityCalories = []

    for i in range(day_count): 
        list_activityCalories.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #2 : calories : The top level time series for calories burned inclusive of BMR, tracked activity, and manually logged activities.
    activities_calories = auth2_client.time_series("activities/calories",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-calories'])
    info = json.loads(data_dump)

     #add the data to a list
    list_calories = []

    for i in range(day_count): 
        list_calories.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #3 : caloriesBMR :Value includes only BMR calories.
    activities_calories = auth2_client.time_series("activities/caloriesBMR",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-caloriesBMR'])
    info = json.loads(data_dump)

     #add the data to a list
    list_caloriesBMR = []

    for i in range(day_count): 
        list_caloriesBMR.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #4 : distance
    activities_calories = auth2_client.time_series("activities/distance",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-distance'])
    info = json.loads(data_dump)

    #add the data to a list
    list_distance = []

    for i in range(day_count): 
        list_distance.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #5 : minutesSedentary
    activities_calories = auth2_client.time_series("activities/minutesSedentary",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-minutesSedentary'])
    info = json.loads(data_dump)

     #add the data to a list
    list_minutesSedentary = []

    for i in range(day_count): 
        list_minutesSedentary.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #6 : minutesLightlyActive
    activities_calories = auth2_client.time_series("activities/minutesLightlyActive",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-minutesLightlyActive'])
    info = json.loads(data_dump)

     #add the data to a list
    list_minutesLightlyActive = []

    for i in range(day_count): 
        list_minutesLightlyActive.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #7 : minutesLightlyActive
    activities_calories = auth2_client.time_series("activities/minutesFairlyActive",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-minutesFairlyActive'])
    info = json.loads(data_dump)

     #add the data to a list
    list_minutesFairlyActive = []

    for i in range(day_count): 
        list_minutesFairlyActive.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #8: minutesVeryActive
    activities_calories = auth2_client.time_series("activities/minutesVeryActive",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-minutesVeryActive'])
    info = json.loads(data_dump)

     #add the data to a list
    list_minutesVeryActive = []

    for i in range(day_count): 
        list_minutesVeryActive.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #9: steps
    activities_calories = auth2_client.time_series("activities/steps",base_date=start_date,end_date=end_date)
    data_dump = json.dumps(activities_calories['activities-steps'])
    info = json.loads(data_dump)

    #add the data to a list
    list_steps = []

    for i in range(day_count): 
        list_steps.append(info[i]['value'])

    #-------------------------------------------------------------------------------------------------------------
    #creation of a dictionary with all the list
    dict = {'date' : date_list, 'activity-calories' : list_activityCalories, 'calories' : list_calories, 'caloriesBMR' : list_caloriesBMR,
            'distance' : list_distance, 'minutesSedentary' : list_minutesSedentary,'minutesLightlyActive' : list_minutesLightlyActive,
            'minutesFairlyActive' : list_minutesFairlyActive, 'minutesVeryActive' : list_minutesVeryActive,'steps' : list_steps }
    df = pd.DataFrame(dict)
    
    #dictornary to csv 
    df.to_csv("source/data/activities.csv",index=False)