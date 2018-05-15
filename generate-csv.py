import pandas as pd
import csv
import os
import glob


path =r'/Users/MRajS/Documents/my_project_work/MONROE/github-my-browsertime/browsertime-debug/working/headless-parsed-logs' # use your path
allFiles = glob.glob(path + "/*.txt")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,sep=';',names = ["url", "protocol", "browser", "operator","num_objects"])
    list_.append(df)
result = pd.concat(list_)
result.to_csv('all-data.csv', sep=',')
