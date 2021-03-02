import tweepy
import csv
from datetime import datetime
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Authenticate to Twitter
auth = tweepy.OAuthHandler("hEhS0TwRGledDHUtMzOyfuYrS",
                            "4xkPmjqYBuPyefFrmCsYPIhQuRvydDXwzyQS7E6OSr6FwnpBTm")
auth.set_access_token("1328566149642997760-FBM6Ti2HnfbmFWLNnfULRAVFkHUdFX",
                          "q1L5tJKFLQ485UHyC6wsLqy4GgMRaHRkecmh5Gaj92quy")

# Create API object
api = tweepy.API(auth)

id = 1347976583944962048 #https://twitter.com/BleacherReport/status/1347976583944962048

status = api.get_status(id) 

favoriteC = status.favorite_count
retweetC = status.retweet_count
            
now = datetime.now()

currentDate = now.strftime("%m/%d/%y")
currentTime = now.strftime("%I:%M:%S %p")

file = "/Users/ch_kus/Desktop/TwitterBasketball.csv"
    
with open(file, mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow([currentDate, currentTime, favoriteC, retweetC])

