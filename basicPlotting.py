import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as pyplot


data = pd.ExcelFile("all_results.xlsx")
df=data.parse("all_results")
df.head()

g=sns.boxplot(x="Browser", y="Plt", hue="Protocol",data=df, palette="PRGn")
sns.despine(offset=10, trim=True)
pyplot.show()


g=sns.boxplot(x="Browser", y="SI", hue="Protocol",data=df, palette="PRGn")
sns.despine(offset=10, trim=True)
pyplot.show()


g=sns.boxplot(x="Browser", y="FirstPaint", hue="Protocol",data=df, palette="PRGn")
sns.despine(offset=10, trim=True)
pyplot.show()


g=sns.factorplot(x="Browser",y="Plt", hue="Protocol",col="Url", data=df,kind="bar",col_wrap=5)
pyplot.show()
