#numpy will enableus to work with multi-dimensional arrays so good for large data
import numpy as np
#pandas allows us to organise data in tabular form and allows data manipulation using these tables
import pandas as pd
#scipy contains tools for scientific calculation
import scipy
#
import statsmodels.api as sm
#matpltlib allows us to create 2D visualisations
import matplotlib.pyplot as plt
#seaborn is for drawing statistical graphics
import seaborn as sns
#
import sklearn

print('Checkpoint: Packages imported successfully!')

#Read data into dataframe from file located in the current directory
#In this example, we 2 columns, SAT score and GPA
#The goal is to predict the GPA based on SAT score
data = pd.read_csv('1.01. Simple linear regression.csv')

#The line below gives statistical sumaaries of the data like count, mean, percentiles and so on for each column
data_description = data.describe()

#Regression model follows y = b0 + b1*x1
#y - predicted value
#
y = data['GPA']
x1 = data['SAT']

#plot the (observed) data that we have so far in a scatter plot
plt.scatter(x1,y)
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
# plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()
