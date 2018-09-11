import requests

r = requests.get('http://wwww.yelp.com')
if r.status_code == 200:
    print r.content


# Assignment 

# Load the yelp page and replace all occurance of yelp to google
# Load the file from http://censusdata.ire.org/36/all_050_in_36.P2.csv and find
# the max P002001

