import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import csv
import os
import json

urls_list=["live","youtube","reddit",
           "wikipedia","yelp","facebook","microsoft",
           "imgur","instagram","coursera","stackoverflow",
           "ebay","tmall","twitter","kayak",
           "theguardian","etsy","flickr"]
#urls_list=["live"]

pyplot.rcParams.update({'figure.max_open_warning': 0})
result=pd.read_csv('browsertime-nr.csv')

def plot_it(ops,url):

	pyplot.clf()
	sns.set_context('paper')
	pyplot.figure(figsize=(5, 3))
	sns.set(font_scale=0.7)
	metric="pageLoadTime"
	browser="Firefox"
	my_browser=result.browser==browser
	my_ops=result.Ops==ops
	my_url=result.url==url
	
	data=result[my_browser & my_ops & my_url ]
	
	data[metric]=data[metric]/1000
	
	h1=data["protocol"]=="HTTP1.1/TLS"
	h2=data["protocol"]=="HTTP2"
	
	
	g=sns.kdeplot(data[h1].pageLoadTime,cumulative=True, label="HTTP1.1/TLS-"+browser)
	g=sns.kdeplot(data[h2].pageLoadTime,cumulative=True, label="HTTP2-"+browser)
	
	browser="Chrome"
	my_browser=result.browser==browser
	my_ops=result.Ops==ops
	my_url=result.url==url
	
	data=result[my_browser & my_ops & my_url]
	
	
	data[metric]=data[metric]/1000
	
	h1=data["protocol"]=="HTTP1.1/TLS"
	h2=data["protocol"]=="HTTP2"
	
	
	g=sns.kdeplot(data[h1].pageLoadTime,cumulative=True, label="HTTP1.1/TLS-"+browser)
	g=sns.kdeplot(data[h2].pageLoadTime,cumulative=True, label="HTTP2-"+browser)
	#g.set_xscale('log')

	pyplot.xlabel("PLT [s]")
	pyplot.ylabel("CDF")
	
	for short_url in urls_list:
	        if short_url in url:
			pyplot.title(ops+"-"+short_url)
			ops.replace(" ","-")
			pyplot.xlim(0,30)
			pyplot.savefig("plt_graphs/"+ops+"-"+short_url+"-"+"plt"+".pdf")
	
urls=result.url.unique()
ops=result.Ops.unique()

#ops="Orange (ES)"
#plot_it(ops,"www.live.com")
for url in urls:
	for op in ops:
		plot_it(op,url)
