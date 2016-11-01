import time
import random
import math
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split

## read and organize data
solar={}
# import solar energy data
for line in open('openpv_copy.csv'):
    index,state,size,cost,date,lat,lon,zipcode=line.strip().split(',')
    if state=='CA':
        solar.setdefault((zipcode),[])
        # Add details to the list of possible routes
        solar[(zipcode)].append((size,cost,date))
print(solar)
    
census={}
# import census data
for line in open('census.csv'):
    index,zipcode,households,income,white,black=line.strip().split(',')
    census.setdefault((zipcode),[])
    # Add details to the list of possible routes
    census[(zipcode)].append((households,float(income),int(white),int(black)))
print(census)

## clean data
def getyear(t):
    x=time.strptime(t,'%M/%D/%Y')
    month=t[0]
    day=t[1]
    year=t[2]
    return year

def makearray(d):
    for i in d:
        X, y = np.array(i[0]).reshape((len(d)/2, 2)), range(5)
        
    
# generate other variables 
def getmix(s):
    for i in census:
        households=census[i][0]
        black=census[i][3]/households
        white=census[i][3]/households
        #mix=black/households # or try this
        if black > 70% or white > 70%:
            mix=0
        else:
            mix = 1
    return mix

# plot relationship between income, race and size
def getplot(x,y):
    plot(x,y)
# split data for training 
# regression on new data
# visualization
# insights