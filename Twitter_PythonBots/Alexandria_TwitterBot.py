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

id = 1347978647454576642 #https://twitter.com/AOC/status/1347978647454576642

status = api.get_status(id) 

favoriteC = status.favorite_count
retweetC = status.retweet_count
            
now = datetime.now()

currentDate = now.strftime("%m/%d/%y")
currentTime = now.strftime("%I:%M:%S %p")

file = "/Users/ch_kus/Desktop/TwitterAlexandria.csv"
    
with open(file, mode='a') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow([currentDate, currentTime, favoriteC, retweetC])




