#!/usr/bin/python

with open("N4xFilterTier") as f:
    # Reading lines in form of lists
    lines = f.readlines()

for line in lines:
    print line


## Assignment

# Parse the ny-census.csv file, and print the rows with POP100 clumn is more than 50477
# Find the row with maxium value in column POP100