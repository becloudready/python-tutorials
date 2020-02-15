import numpy as np
import pandas as pd
import csv
import os

os.getcwd()

os.chdir('.')

os.getcwd()




#importing data from computer and other locations

newdata = pd.read_csv('sample.csv')

#newdata = pd.read_csv('E:\\Shailendra\\Personal\\TR\\sample_data\\Sample_csv_File_V1.csv')

#checking the data


#gives stats about numerical variables
checkingdata = newdata.describe()

#allows us to view first X observations
newdata.head()

#getting frequency table of a single variable
newdata['age'].value_counts()



print(newdata.columns) # prints the column names

newdata1=newdata
# reading a csv file with options






#Group by 


newdata1.agg({'age':'mean'})


print(newdata1['age'].mean())

print(newdata1['age'].median())

print(newdata1['age'].std())


#Defining a function

#Example 1

def greetings(name):
	"""This function greets to the person passed in as	parameter"""
	print("Hello, " + name + ". Good morning!")
    

#Calling a function

greetings("Bo")    

#Example 2

def cube(num):
	"""This function returns the cube of the entered number"""

	if num >= 0:
		return num*num*num
	else:
		return "negative"
    
cube(9)
cube(-9)

#Parameters = Information can be passed to functions as parameter.

def my_function(fname):
  print(fname + " is a Data Scientist")

my_function("Bo")
my_function("Chandan")
my_function("Shailendra")

import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/biz/after-dark-toronto"

r = requests.get(url);

# Collect all the reviews elements on the current page.
soup = BeautifulSoup(r.text, 'lxml')
#for review_block in soup('div', {'itemprop': 'review'}):
    
reviewer = review_block.find("meta", {"itemprop":"author"})['content']
print (reviewer)


rating = review_block.find('meta', {'itemprop': 'ratingValue'})['content']
print (rating)

feedback = review_block.find('p', {'itemprop': 'description'}).get_text();
print (feedback)


import  twitter
from twitter import Twitter
from twitter import OAuth
consumer_key = ""
consumer_secret = "" 
access_token = ""
access_token_secret = ""
oauth=  OAuth(access_token,access_token_secret,consumer_key,consumer_secret)
api= Twitter(auth=oauth)


import pandas as pd
from textblob import TextBlob

search_results = api.search.tweets(q="trump", count=2)
#print (search_results)

data = []
for tweet in search_results['statuses']:
    print (tweet['text'])
    print(TextBlob(tweet['text']))
    print(TextBlob(tweet['text']).sentiment.polarity)

