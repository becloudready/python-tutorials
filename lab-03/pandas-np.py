#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:37:49 2020
Copyright: beCloudReady

@author: Chandan Kumar
"""


import numpy as np
import pandas as pd
import csv
import os

print ("Hello World!")


os.getcwd()

os.chdir('.')

os.getcwd()

#importing data from computer and other locations

newdata = pd.read_csv('../dataset/sample.csv')

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



print(newdata1['age'].mean())

print(newdata1['age'].median())

print(newdata1['age'].std())


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


def my_function(fname):
  print(fname + " is a Data Scientist")

my_function("beCloudReady")
my_function("Chandan")
my_function("Shailendra")
