# TwitterViralityResearchProject

I initiated a research project in UCSC to analyze how Twitter virality behaves using Python, Tweepy, and Pandas.
I designed three Python bots that parse Twitter API using Tweepy to gather data on three sample Twitter accounts.
The results were then amalgamated into CSV files and I uploaded them to Pandas to create graphs to analyze the data.


## Getting Started

These instructions will describe each segment of the project and it's purpose.

## Stage One: Setting up Sampling (Navigating Twitter_PythonBots)

This folder contains the three Python Twitter bots: Marq_TwitterBot.py, Basketball_TwitterBot.py, and Alexandria_TwitterBot.py. I created each Python Bot to parse Twitter API data on Tweepy to scan the favorite and retweet counts of sample tweets from these accounts: https://twitter.com/AOC, https://twitter.com/BleacherReport, and https://twitter.com/MKBHD. 

#### Id Parameter:
```
id = 1347978647454576642 #https://twitter.com/AOC/status/1347978647454576642
#Contains the sample tweet's id
```

#### Other Parameters
```
favoriteC = status.favorite_count #contains sample tweet's favorite count
retweetC = status.retweet_count   #contains sample tweet's retweet count
            
now = datetime.now()

currentDate = now.strftime("%m/%d/%y") #contains sample tweet's date
currentTime = now.strftime("%I:%M:%S %p") #contains sample tweet's time
```

## Stage Two: Sampled data (Navigating csv_data)

This folder contains the three directories: Alexandria_data, Marques_brownlee_data, and basketball_data. The Marques_brownlee_data and basketball_data directories contain three different csv files, denoting different interval samples: 1 hour sample, 3 hour sample, 12 hour sample. The  Alexandria_data contains only the 3 hour sample annd 12 hour sample csv data. 

#### Example marq_1hr.csv contents:
```
DataTime Column #The dates I sampled Marq_TwitterBot.py.

Favorites Column #The sampled favorite count of a tweet I sampled using Marq_TwitterBot.py.

Retweet Column #The sampled retweet count of a tweet I sampled using Marq_TwitterBot.py.
```

## Stage Three: Analyzing data (Navigating Pandas_data_analysis)

This folder contains the three directories: Alexandria_data, Marques_brownlee_data, and basketball_data. The Marques_brownlee_data and basketball_data directories contain three different ipynb files, denoting the analysis of different csv data samples: 1 hour csv data, 3 hour csv data, 12 csv data. The  Alexandria_data contains only the analysis of the 3 hour csv data and 12 hour csv data. 

#### Example Alexandra_3hr.ipynb contents:

##### Cell 1
```
#Contains all the necessary imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
```

##### Cell 2 Date Time vs Favorites Cell
```

#Prints the Date Time vs Favorites graph of Alexandria 3 hour csv data.

dataFrame_alexandria = pd.read_csv('/Users/ch_kus/Desktop/alexandria_3hr.csv')
dataFrame_alexandria = dataFrame_alexandria[0:10]
dataFrame_alexandria["DateTime"] = pd.to_datetime(dataFrame_alexandria['DateTime'])
var = dataFrame_alexandria["DateTime"]

%matplotlib inline
plt.title("Alexandria Politics Favorites vs DateTime")
plt.xlabel("Date Time")
plt.ylabel("Favorite Count")
plt.plot(var, dataFrame_alexandria.Favorites)
```

##### Cell 3 Derivative Graph (Favorites vs DateTime)
```
derivativeList = dataFrame_alexandria.Favorites.diff()

%matplotlib inline
plt.title("Alexandria Politics Favorites vs DateTime Derivative")
plt.xlabel("Date Time")
plt.ylabel("Favorite Count")
plt.plot(var, derivativeList)
```

##### Cell 4 Date Time vs Retweets Cell
```
%matplotlib inline
plt.title("Alexandria Politics Retweets vs DateTime")
plt.xlabel("Date Time")
plt.ylabel("Retweet Count")
plt.plot(var, dataFrame_alexandria.Retweets)
```
##### Cell 5 Derivative Graph (Retweets vs DateTime)
```
derivativeList_r = dataFrame_alexandria.Retweets.diff()

%matplotlib inline
plt.title("Alexandria Politics Retweets vs DateTime Derivative")
plt.xlabel("Date Time")
plt.ylabel("Retweet Count")
plt.plot(var, derivativeList_r)
```
##### Cell 6 Favorites vs Retweets Cell
```
plt.plot(dataFrame_alexandria.Favorites, dataFrame_alexandria.Retweets)
```
##### Cell 7 Favorites vs Retweets Cell
```
#calculates the pearson correlation of favorites vs retweets
dataFrame_alexandria.corr(method ='pearson')
```

## Built With

* [Pandas](https://pypi.org/project/pandas/) - The Python Data Analysis Library 
* [Tweepy](https://www.tweepy.org/) - Used to parse for Twitter API user data
* [IDLE](https://docs.python.org/3/library/idle.html) - Used to create Python Bots

## Authors

* **Kushal Chigati** - *Initial work* - [KushalChi](https://github.com/KushalChi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
