import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import csv
import os
import json
import glob
path =r'/Users/MRajS/Documents/my_project_work/MONROE/github-my-browsertime/browsertime-debug/working/headless-parsed-logs' # use your path
allFiles = glob.glob(path + "/*.txt")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,sep=';',names = ["url", "protocol", "browser", "operator","num_objects"])
    list_.append(df)
frame_all = pd.concat(list_)
print frame_all.head()
frame=frame_all[frame_all.url=="www.tmall.com"]
print frame.head()
g = sns.FacetGrid(frame, row="operator", col="browser", margin_titles=True)
g.map(pyplot.hist, "num_objects", color="steelblue",  lw=0)
pyplot.yscale('log')
pyplot.savefig("tmall.pdf")
