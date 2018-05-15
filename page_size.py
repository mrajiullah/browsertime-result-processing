import matplotlib
import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd

length=[]
size=[]

#with open('sorted_lenght_size_chrome') as f:
#    for line in f:
#	line.rstrip()
#        l, s = line.split(' ')
#	length.append(int(l))
#	size.append(float(s))

#print length
#print size

df = pd.read_csv("sorted_lenght_size_chrome", sep=' ', 
                  names = ["length", "size"])

print df
# Set style of scatterplot
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")


# Create scatterplot of dataframe
sns.lmplot('length', # Horizontal axis
           'size', # Vertical axis
           data=df, # Data source
           fit_reg=False, # Don't fix a regression line
          # hue="z", # Set color
           scatter_kws={"marker": "D", # Set marker style
                        "s": 100}) # S marker size

# Set title
pyplot.title('Size of pages used in the test')

# Set x-axis label
pyplot.xlabel('Number of Objects')

# Set y-axis label
pyplot.ylabel('Size (kB)')

#pyplot.scatter(length,size)
pyplot.savefig("page_size.pdf")
