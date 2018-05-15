import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns

data=pd.read_csv('browsertime.csv')
result=data
result['protocol'].replace(["HTTP1.1/TLS","HTTP2"],
                           ["H1s","H2"],inplace=True)
result["rumSpeedIndex"]=result["rumSpeedIndex"]/1000
brs=result.browser.unique()
for br in brs:
    pyplot.clf()
    sns.set_context('paper')
    pyplot.figure(figsize=(18, 10))
    sns.set(font_scale=2.2)
    #sns.set_style("white")
    g=sns.boxplot(x="Ops", y="rumSpeedIndex", hue="protocol",data=result[(result.browser==br)],
                  order=["Telia (SE)", "Telenor (SE)", "Tre (SE)", "Telenor (NO)", "Telia (NO)", "ICE (NO)", "TIM (IT)",
                         "Vodafone (IT)", "Wind (IT)","Orange (ES)","Yoigo (ES)"],hue_order=["H1s","H2"],palette="muted",showfliers=False)
    pyplot.xticks(rotation=10)
    pyplot.title(br)
    pyplot.ylabel("SI")
    pyplot.xlabel("Operators")
    pyplot.savefig("final_graphs/"+br+"-si.pdf")
