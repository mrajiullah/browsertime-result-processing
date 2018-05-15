import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import csv
import os
import json


result=pd.read_csv('browsertime.csv')

def plot_it(browser,country,metric):

	my_browser=result.browser==browser
	my_country=result.Country==country

	data=result[my_browser & my_country]

	data[metric]=data[metric]/1000

	h1=data["protocol"]=="HTTP1.1/TLS"
	h2=data["protocol"]=="HTTP2"



	g=sns.kdeplot(data[h1].pageLoadTime,cumulative=True, label="HTTP1.1/TLS")
	g=sns.kdeplot(data[h2].pageLoadTime,cumulative=True, label="HTTP2")
	g.set_xscale('log')
	pyplot.xlabel(metric)
	pyplot.ylabel("CDF")
	pyplot.title(browser+"-"+country)
	pyplot.savefig("final_graphs/"+browser+country+metric+".pdf")

plot_it("Firefox","SE","pageLoadTime")
