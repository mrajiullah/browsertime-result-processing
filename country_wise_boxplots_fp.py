import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import csv
import os
import json

data=pd.read_csv('browsertime-data.csv')
data['protocol'].replace(["HTTP1.1/TLS","HTTP2"],
                           ["H1s","H2"],inplace=True)

from pylab import rcParams
rcParams['figure.figsize'] = 10,5

fig = pyplot.figure()
fig.subplots_adjust(hspace=.5)

ax1 = fig.add_subplot(321)

sns.boxplot(x="Ops",y="firstPaint", hue="protocol",data=data[(data.Country=="IT")],
            order=["TIM (IT)",
                   "Vodafone (IT)", "Wind (IT)"],
            hue_order=["H1s","H2"],palette="muted",showfliers=False)
#pyplot.figure(figsize=(4,2))
#pyplot.xlabel("Operator")
ax1.set_xlabel('')
pyplot.ylabel("First Paint")
ax1.legend_.remove()
#ax1.text(0.85, 11.85,'Italy', fontsize=14)
	

for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label] +
             ax1.get_xticklabels() + ax1.get_yticklabels()):
    item.set_fontsize(16)


ax2 = fig.add_subplot(322)
sns.boxplot(x="Ops",y="firstPaint", hue="protocol",data=data[(data.Country=="ES")],
            order=["Orange (ES)","Yoigo (ES)"],
            hue_order=["H1s","H2"],palette="muted",showfliers=False)
#pyplot.figure(figsize=(4,2))
##pyplot.xlabel("Operator")
ax2.set_ylabel('')    
ax2.set_xlabel('')
ax2.legend_.remove()
#ax2.text(0.85, 11.85,'Spain', fontsize=14)
for item in ([ax2.title, ax2.xaxis.label, ax2.yaxis.label] +
             ax2.get_xticklabels() + ax2.get_yticklabels()):
    item.set_fontsize(16)

ax3 = fig.add_subplot(323)
sns.boxplot(x="Ops",y="firstPaint", hue="protocol",data=data[(data.Country=="NO")],
            order=["Telenor (NO)", "Telia (NO)", "ICE (NO)"],
            hue_order=["H1s","H2"],palette="muted",showfliers=False)
#pyplot.figure(figsize=(4,2))
pyplot.xlabel("Operators")
pyplot.ylabel("First Paint")
ax3.legend_.remove()
#ax3.text(0.85, 10.85,'Norway', fontsize=14)

for item in ([ax3.title, ax3.xaxis.label, ax3.yaxis.label] +
             ax3.get_xticklabels() + ax3.get_yticklabels()):
    item.set_fontsize(16)

ax4 = fig.add_subplot(324)

sns.boxplot(x="Ops",y="firstPaint", hue="protocol",data=data[(data.Country=="SE")],
            order=["Telia (SE)", "Telenor (SE)", "3 (SE)"],
            hue_order=["H1s","H2"],palette="muted",showfliers=False)
pyplot.xlabel("Operators")
ax4.set_ylabel('')    
#ax4.text(0.010, 15.85,'Sweden', fontsize=14)
for item in ([ax4.title, ax4.xaxis.label, ax4.yaxis.label] +
             ax4.get_xticklabels() + ax4.get_yticklabels()):
    item.set_fontsize(16)


ax4.legend_.remove()
#ax4.legend(loc='center left', bbox_to_anchor=(0.3, 0.7))

ax5 = fig.add_subplot(325)
ax5.set_axis_off()  #turn off the axis 
ax5.legend(loc='center left', bbox_to_anchor=(0.3, 0.7))


pyplot.savefig("country_wise_boxplots_fp.pdf")
