import pandas as pd

df=pd.read_csv("browsertime.csv")

df_nr=df[df['roaming'] == 0]
df_r=df[df['roaming'] == 1]

#print df_r.roaming.value_counts()
print df_nr.Ops.value_counts()
print "Roaming"
print df_r.Ops.value_counts()

df_nr.to_csv("browsertime-nr.csv")
df_r.to_csv("browsertime-r.csv")

