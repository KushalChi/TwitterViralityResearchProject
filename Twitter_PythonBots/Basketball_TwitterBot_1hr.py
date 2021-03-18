#################################################################################################################
# Created by:  Kushal
#
# Description: Basketball Twitter Bot 1 HOUR - https://github.com/KushalChi/TwitterViralityResearchProject
#
# Notes:       This program is intended to be run from the Python IDLE or any Python environment.
#################################################################################################################

import tweepy
import csv
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

'''Authenticate to Twitter - It is important to provide your Twitter Tweepy dev account information into
these objects here. The following link details the significance of each of these consumer keys and access tokens:
https://docs.tweepy.org/en/latest/auth_tutorial.html'''

auth = tweepy.OAuthHandler(Enter consumer_key..., Enter consumer_secret...)
auth.set_access_token(Enter access_token..., Enter access_token_secret...)

#Create TwitterAPI object
api = tweepy.API(auth)

id = 1360618567285153799 #https://twitter.com/BleacherReport/status/1360618567285153799

status = api.get_status(id) #Retrieves status for sample tweet

favoriteC = status.favorite_count #Retrieves favorite count of sample tweet 
retweetC = status.retweet_count   #Retrieves retweet count of sample tweet 
            
now = datetime.now() #Retrieves current time of sample tweet 

currentDate = now.strftime("%m/%d/%y")    #Formats Date using month/day/year format
currentTime = now.strftime("%I:%M:%S %p") #Formats Time using hour/minute/second format

file = "Enter your file path to where basketball_1hr.csv is located here" 
    
with open(file, mode='a') as employee_file: #Opens the basketball_1hr.csv file and writes the data to it
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow([currentDate, currentTime, favoriteC, retweetC])








