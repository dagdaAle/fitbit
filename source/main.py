import csv
from csv import reader
import datetime
import mysqlx
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
 

#start date 
day_inizio = input("inserisci il giorno di inizio : ")
month_inizio = input("inserisci il mese di inizio : ")
year_inizio = input("inserisci il anno di inizio : ")

#end date 
day_fine = input("inserisci il giorno di fine : ")
month_fine = input("inserisci il mese di fine : ")
year_fine = input("inserisci il giorno di fine : ")

#define start and end date
start_date = datetime.datetime(int(year_inizio),int(month_inizio),int(day_inizio)).date()
end_date = datetime.datetime(int(year_fine),int(month_fine),int(day_fine)).date()

print(start_date)
print(end_date)

#import functions
import activity
import sleep
import user
import heartrate
import date_ranges
date_ranges = date_ranges.generateDateRange(start_date,end_date)
list_user = user.getuser()
heartrate.getheartrate(start_date,end_date)

print(date_ranges)


#insert activity data in the database
activity.getactivity(start_date,end_date)
path = "source\data\\activities.csv"
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       #print(row)
        list_row = row
        my_list= list_user + list_row
        print(my_list)
        try:
                conn = mysql.connect(host='localhost', database='fitbit', user='root', password='Progetto.fitbit22')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    #create table if it dosn't exist
                    cursor.execute("""CREATE TABLE IF NOT EXISTS `fitbit`.`activity` (
                                    `id` INT NOT NULL AUTO_INCREMENT,
                                    `user_id` VARCHAR(45) NULL,
                                    `user_name` VARCHAR(45) NULL,
                                    `user_age` VARCHAR(45) NULL,
                                    `date` VARCHAR(45) NULL,
                                    `activity_calories` INT NULL,
                                    `calories` INT NULL,
                                    `caloriesBMR` INT NULL,
                                    `distance` INT NULL,
                                    `minutesSedentary` INT NULL,
                                    `minutesLightlyActive` INT NULL,
                                    `minutesFairlyActive` INT NULL,
                                    `minutesVeryActive` INT NULL,
                                    `steps` INT NULL,
                                    PRIMARY KEY (`id`));""")

                    #execution of the query
                    cursor.execute('INSERT INTO fitbit.activity(user_id, user_name,user_age, date, activity_calories, calories, caloriesBMR, distance, minutesSedentary, minutesLightlyActive, minutesFairlyActive, minutesVeryActive, steps)''VALUES(%s , %s , %s , %s , %s , %s, %s , %s , %s, %s , %s , %s, %s)',my_list)
                    conn.commit()     
                    
        except Error as e:
                        print("Error while connecting to MySQL", e)


#insert sleep data in the database
sleep.getsleep(start_date,end_date)
path = "source\data\\sleep.csv"
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       #print(row)
        list_row = row
        my_list= list_user + list_row
        print(my_list)
        try:
                conn = mysql.connect(host='localhost', database='fitbit', user='root', password='Progetto.fitbit22')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    #create table if it dosn't exist
                    cursor.execute("""CREATE TABLE IF NOT EXISTS `fitbit`.`sleep` (
                                    `id_sleep` INT NOT NULL AUTO_INCREMENT,
                                    `user_id` VARCHAR(45) NULL,
                                    `user_name` VARCHAR(45) NULL,
                                    `user_age` VARCHAR(45) NULL,
                                    `date_of_sleep` VARCHAR(45) NULL,
                                    `awakeCount` INT NULL,
                                    `awakeDuration` INT NULL,
                                    `awakeningsCount` INT NULL,
                                    `duration` INT NULL,
                                    `efficiency` INT NULL,
                                    `minutesAfterWakeup` INT NULL,
                                    `minutesAsleep` INT NULL,
                                    `minutesAwake` INT NULL,
                                    `minutesToFallAsleep` INT NULL,
                                    `restlessCount` INT NULL,
                                    `restlessDuration` INT NULL,
                                    `timeInBed` INT NULL,
                                    PRIMARY KEY (`id_sleep`));""")

                    #execution of the query
                    cursor.execute('INSERT INTO fitbit.sleep(user_id, user_name, user_age, date_of_sleep, awakeCount, awakeDuration, awakeningsCount, duration, efficiency, minutesAfterWakeup, minutesAsleep, minutesAwake, minutesToFallAsleep, restlessCount, restlessDuration, timeInBed)''VALUES(%s , %s , %s , %s , %s , %s, %s , %s , %s, %s , %s , %s, %s, %s, %s, %s)',my_list)
                    conn.commit()     
                    
        except Error as e:
                        print("Error while connecting to MySQL", e)


#insert heartrate data in the database
heartrate.getheartrate(start_date,end_date)
path = "source\data\\heart.csv"
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       #print(row)
        list_row = row
        my_list= list_user + list_row
        print(my_list)
        try:
                conn = mysql.connect(host='localhost', database='fitbit', user='root', password='Progetto.fitbit22')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    #create table if it dosn't exist
                    cursor.execute("""CREATE TABLE IF NOT EXISTS `fitbit`.`heartrate` (
                                    `id_heartrate` INT NOT NULL AUTO_INCREMENT,
                                    `user_id` VARCHAR(45) NULL,
                                    `user_name` VARCHAR(45) NULL,
                                    `user_age` VARCHAR(45) NULL,
                                    `dateTime` VARCHAR(45) NULL,
                                    `caloriesOut` INT NULL,
                                    `max` INT NULL,
                                    `min` INT NULL,
                                    `minutes` INT NULL,
                                    `name` VARCHAR(45) NULL,
                                    `restingHeartRate` INT NULL,
                                    PRIMARY KEY (`id_heartrate`));""")

                    #execution of the query
                    cursor.execute('INSERT INTO fitbit.heartrate(user_id,user_name,user_age,dateTime, caloriesOut, max, min, minutes, name, restingHeartRate)''VALUES(%s , %s , %s , %s , %s , %s, %s , %s , %s, %s)',my_list)
                    conn.commit()     
                    
        except Error as e:
                        print("Error while connecting to MySQL", e)



path = "C:\\Users\\aless\\OneDrive\\Desktop\\Tesi_fitbit\\MyFitbitData\\Massimo\\Sleep\\sleep_score.csv"
print(path)

#open the csv 
with open(path, 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
            # row variable is a list that represents a row in csv
            print(row)
            list_row = row
            my_list= list_user + list_row

            #database connection
            try:
                conn = mysql.connect(host='localhost', database='fitbit', user='root', password='Progetto.fitbit22')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)

                    cursor.execute("""CREATE TABLE IF NOT EXISTS `fitbit`.`sleep_score` (
                                    `id_sleep_score` INT NOT NULL AUTO_INCREMENT,
                                    `user_id` VARCHAR(45) NULL,
                                    `user_name` VARCHAR(45) NULL,
                                    `user_age` VARCHAR(45) NULL,
                                    `sleep_log_entry_id` DOUBLE NULL DEFAULT NULL,
                                    `timestamp` VARCHAR(45) NULL,
                                    `overall_score` INT NULL,
                                    `composition_score` INT NULL,
                                    `revitalization_score` INT NULL,
                                    `duration_score` INT NULL,
                                    `deep_sleep_in_minutes` INT NULL,
                                    `resting_heart_rate` INT NULL,
                                    `restlessness` INT NULL,
                                    PRIMARY KEY (`id_sleep_score`));
                                    """)


                    #eseguo la query per inserire la nuova riga nel database
                    cursor.execute('INSERT INTO fitbit.sleep_score(user_id, user_name, user_age, sleep_log_entry_id, timestamp, overall_score, composition_score, revitalization_score, duration_score, deep_sleep_in_minutes, resting_heart_rate, restlessness)''VALUES(%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)',my_list)
                    conn.commit()     
                    
            except Error as e:
                        print("Error while connecting to MySQL", e)