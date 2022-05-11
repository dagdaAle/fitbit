import csv
from csv import reader
import datetime
import mysqlx
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

#capire un modo in cui importaere i file 
#fare inserire il range di date dall utente 
#suicidarsi 
#form per inserimento utente 

user_name =  input("inserisci nome utente : ")
user_surname =  input("inserisci cognome utente : ")
user_age =  input("inserisci età dell utente : ")


day_inizio = input("inserisci il giorno di inizio : ")
month_inizio = input("inserisci il mese di inizio : ")
year_inizio = input("inserisci il anno di inizio : ")

day_fine = input("inserisci il giorno di fine : ")
month_fine = input("inserisci il mese di fine : ")
year_fine = input("inserisci il giorno di fine : ")


start_date = datetime.datetime(int(year_inizio),int(month_inizio),int(day_inizio)).date()
end_date = datetime.datetime(int(year_fine),int(month_fine),int(day_fine)).date()

print(start_date)
print(end_date)

import activity
import sleep
sleep.getsleep(start_date,end_date)
activity.getactivity(start_date,end_date)

#
#CREATE TABLE `fitbit`.`activity` (
#  `id` INT NOT NULL AUTO_INCREMENT,
#  `user_name` VARCHAR(45) NULL,
#  `user_surname` VARCHAR(45) NULL,
#  `user_age` VARCHAR(45) NULL,
#  `date` VARCHAR(45) NULL,
#  `activity_calories` INT NULL,
#  `calories` INT NULL,
#  `caloriesBMR` INT NULL,
#  `distance` INT NULL,
#  `minutesSedentary` INT NULL,
#  `minutesLightlyActive` INT NULL,
#  `minutesFairlyActive` INT NULL,
#  `minutesVeryActive` INT NULL,
#  `steps` INT NULL,
#  PRIMARY KEY (`id`));

path = "source\data\\activities.csv"
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        try:
                conn = mysql.connect(host='localhost', database='fitbit5', user='root', password='sarisapa')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)

                    #eseguo la query per inserire la nuova riga nel database
                    cursor.execute('INSERT INTO fitbit.activity(date, activity_calories, calories, caloriesBMR, distance, minutesSedentary, minutesLightlyActive, minutesFairlyActive, minutesVeryActive, steps)''VALUES(%s, %s, %s, %s,%s, %s, %s,%s, %s)',row)
                    conn.commit()     
                    
        except Error as e:
                        print("Error while connecting to MySQL", e)