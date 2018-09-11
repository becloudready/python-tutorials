#!/usr/bin/python

my_string = "My string has many spaces let me see how many"

print my_string.split()

print "Lets loop through the strings"

for s in my_string.split():
    print ("String literal ", s)

my_string = "My,string,has,many,commas,let,me,see,how,many"

# Assignment
# Count number of , in the string
# Replace , with space
# Count the string length
# Find the index where the word many starts
