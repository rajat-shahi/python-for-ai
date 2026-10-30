# Pattern-1 : import the whole module
import math 
math.sqrt(25)


# pattern 2 : import specific items from a module
from math import sqrt,pi,pow
print(pow(2,5)) 

# Import with alias
import pandas as pd 


# datetime module
import datetime 
today = datetime.date.today()
print(today)


# operating system 
import os
curr_dir = os.getcwd()
print(curr_dir)

# JSON data 
import json 
data = {"name":"rajat","age":26}
json_string = json.dumps(data)
print(json_string)


# NOTE : 
# - Avoid 'from 'x' import *'
# Installing specific version of something : pip install requests==2.14.4
# pip install pandas numpy matplotlib
