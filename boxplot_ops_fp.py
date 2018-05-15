import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns

data=pd.read_csv('browsertime.csv')
#result=data[data.Ops!="Orange (ES)"]
#result.drop(result.columns[[0, 1]], axis=1, inplace=True)
result=data[data.browser=="Firefox"]
result['protocol'].replace(["HTTP1.1/TLS","HTTP2"],
                           ["H1s","H2"],inplace=True)
urls_list=["live","youtube","google","reddit",
	   "wikipedia","yelp","facebook","microsoft",
	   "imgur","instagram","coursera","stackoverflow",
	   "ebay","linkedin","tmall","twitter","kayak",
	   "theguardian","etsy","flickr"]

result["firstPaint"]=result["firstPaint"]/1000

urls=result.url.unique()
for url in urls:
    pyplot.clf()
    sns.set_context('paper')
    pyplot.figure(figsize=(18, 10))
    sns.set(font_scale=2.2)
    #sns.set_style("white")
    g=sns.boxplot(x="Ops", y="firstPaint", hue="protocol",data=result[(result.url==url)],
                  order=["Telia (SE)", "Telenor (SE)", "Tre (SE)", "Telenor (NO)", "Telia (NO)", "ICE (NO)", "TIM (IT)",
                         "Vodafone (IT)", "Wind (IT)","Orange (ES)","Yoigo (ES)"],hue_order=["H1s","H2"],palette="muted",showfliers=False)
    pyplot.xticks(rotation=10)
    pyplot.title(url+"_Firefox")
    pyplot.ylabel("First Paint [s]")
    pyplot.xlabel("Operators")
    for short_url in urls_list:
	if short_url in url:
    		pyplot.savefig("final_graphs/"+short_url+"-fp-firefox.pdf")
