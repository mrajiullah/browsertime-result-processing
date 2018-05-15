import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import csv
import os
import json

urls_list=["live","youtube","google","reddit",
           "wikipedia","yelp","facebook","microsoft",
           "imgur","instagram","coursera","stackoverflow",
           "ebay","linkedin","tmall","twitter","kayak",
           "theguardian","etsy","flickr"]

data=pd.read_csv('browsertime.csv')

metric="firstPaint"
browser="Firefox"
url="www.stackoverflow.com"
ops="Orange (ES)"

my_browser=data.browser==browser
my_ops=data.Ops==ops
my_url=data.url==url

data2=data[my_browser & my_ops & my_url ]
print data2.firstPaint.describe()
print data2.rumSpeedIndex.describe()
print data2.pageLoadTime.describe()


h1=data2["protocol"]=="HTTP1.1/TLS"
h2=data2["protocol"]=="HTTP2"

g=sns.kdeplot(data2[h1].firstPaint,cumulative=True, label="HTTP1.1/TLS-"+browser)
g=sns.kdeplot(data2[h2].firstPaint,cumulative=True, label="HTTP2-"+browser)

metric="firstPaint"
browser="Chrome"
url="www.stackoverflow.com"
ops="Orange (ES)"

my_browser=data.browser==browser
my_ops=data.Ops==ops
my_url=data.url==url

data2=data[my_browser & my_ops & my_url ]

h1=data2["protocol"]=="HTTP1.1/TLS"
h2=data2["protocol"]=="HTTP2"

g=sns.kdeplot(data2[h1].firstPaint,cumulative=True, label="HTTP1.1/TLS-"+browser)
g=sns.kdeplot(data2[h2].firstPaint,cumulative=True, label="HTTP2-"+browser)

pyplot.show()
