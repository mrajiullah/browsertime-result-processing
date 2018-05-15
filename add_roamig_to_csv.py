import pandas as pd

df=pd.read_csv("browsertime.csv")

roaming=[]
for index, row in df.iterrows():
	if str(row["IMSIMCCMNC"])[0:3]== str(row["NWMCCMNC"])[0:3]: 
		roaming.append("0")
	else:
		roaming.append("1")
		

df["roaming"]=roaming
#print df["roaming"].value_counts()

df.to_csv("browsertime.csv")
