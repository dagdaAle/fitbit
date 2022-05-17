import csv
from csv import reader
import datetime
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


if __name__ == "__getuser__":
    pass

def getuser() :
    CLIENT_ID='2389G5'
    CLIENT_SECRET='636c18786967602847f7396da3456f41'

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
    auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)

    user = auth2_client.user_profile_get()

    list_user = []
    list_user.append(user["user"]["encodedId"])
    list_user.append(user["user"]["displayName"])
    list_user.append(user["user"]["age"])

    my_list = []
    my_list.append(user["user"]["encodedId"])
    my_list.append(user["user"]["displayName"])
    my_list.append(user["user"]["age"])
    my_list.append(user["user"]["dateOfBirth"])
    my_list.append(user["user"]["gender"])
    my_list.append(user["user"]["height"])
    my_list.append(user["user"]["memberSince"])
    my_list.append(user["user"]["phoneNumber"])
    my_list.append(user["user"]["weight"])

    try:
                conn = mysql.connect(host='localhost', database='fitbit', user='root', password='Progetto.fitbit22')
                if conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute("select database();")
                    record = cursor.fetchone()
                    print("You're connected to database: ", record)
                    #create table if it dosn't exist
                    cursor.execute("""CREATE TABLE IF NOT EXISTS `fitbit`.`user` (
                                    `id_user` VARCHAR(45) NOT NULL,
                                    `name` VARCHAR(45) NULL,
                                    `age` VARCHAR(45) NULL,
                                    `dateofbirth` VARCHAR(45) NULL,
                                    `gender` VARCHAR(45) NULL,
                                    `height` INT NULL,
                                    `memberSince` VARCHAR(45) NULL,
                                    `phoneNumber` VARCHAR(45) NULL,
                                    `weight` INT NULL,
                                    PRIMARY KEY (`id_user`),
                                    UNIQUE INDEX `iduser_UNIQUE` (`id_user` ASC) VISIBLE);""")

                    #execution of the query
                    cursor.execute('INSERT INTO fitbit.user(id_user, name, age, dateofbirth, gender, height, memberSince, phoneNumber, weight)''VALUES(%s , %s , %s , %s , %s , %s, %s , %s , %s)',my_list)
                    conn.commit()     
                    
    except Error as e:
                        print("Error while connecting to MySQL", e)

   
    return list_user
    #ritorno le informazioni di user e eta e id;
   
    #informazione da ritornare come funzione   
    print(user["user"]["age"])
    print(user["user"]["displayName"])
    print(user["user"]["encodedId"])

    #informazioni da far ritornare nella tabella user.
    print(user["user"]["encodedId"])
    print(user["user"]["displayName"])
    print(user["user"]["age"])
    print(user["user"]["dateOfBirth"])
    print(user["user"]["gender"])
    print(user["user"]["height"])
    print(user["user"]["memberSince"])
    print(user["user"]["phoneNumber"])
    print(user["user"]["weight"])
    
getuser()
