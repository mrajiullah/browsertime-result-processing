import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns

data=pd.read_csv('browsertime-data.csv')
result=data[data.Country=="SE"]
#print result.NodeId.value_counts()
#print result.NodeId.unique()
print result.Ops.value_counts()
