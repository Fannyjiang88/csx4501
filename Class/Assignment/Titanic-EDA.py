#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis with the Titanic Dataset
# 
# This dataset is the training dataset from Kaggle's ["Titanic - Machine Learning from Disaster"](https://www.kaggle.com/c/titanic)

# ## Import modules to use Pandas and Matplotlib

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# ## Import the data

# The dataset is contained in a CSV file, "titanic.csv".

# In[2]:


df = pd.read_csv('titanic.csv')


# ## Look at the data
# 
# * look at snapshots of the dataframe
#   * `df`, `df.head()`, `df.tail()`, `df.sample()`
# * look at the sizes
#   * `df.shape`: look at the size of the data
# * look at column names
#   * `df.columns`: look at column names
# * look at summary information
#   * `df.describe()`: statistical summary info
#   * `df.info()`: data types, sizes, column labels, null values

# In[ ]:


df


# In[ ]:


df.head()


# In[3]:


df.shape


# -> There are 891 passengers, 12 columns of features

# In[ ]:


df.columns


# -> These are the column names
# 
# Let's consult information from the Kaggle site to get more information.

# | Variable | Definition | Key| 
# | :-- | :-- | :-- |
# | survival | Survival | 0 = No, 1 = Yes| 
# | pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd| 
# | sex | Sex | | 
# | Age | Age in years | | 
# | sibsp | # of siblings / spouses aboard the Titanic | | 
# | parch | # of parents / children aboard the Titanic | | 
# | ticket | Ticket number | | 
# | fare | Passenger fare | | 
# | cabin | Cabin number | | 
# | embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton| 

# **Variable Notes**
# 
# pclass: A proxy for socio-economic status (SES)
# * 1st = Upper
# * 2nd = Middle
# * 3rd = Lower
# 
# age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
# 
# sibsp: The dataset defines family relations in this way...
# * Sibling = brother, sister, stepbrother, stepsister
# * Spouse = husband, wife (mistresses and fiancés were ignored)
# 
# parch: The dataset defines family relations in this way...
# * Parent = mother, father
# * Child = daughter, son, stepdaughter, stepson
# * Some children travelled only with a nanny, therefore parch=0 for them.

# In[ ]:


df.describe()


# -> What information does this show?
# * average survival rate is 38%
# * age range is 0.42 to 80 yrs old, with mean of ~30
# * at least 50% don't have siblings or spouses
# * fare has higher stdev than mean -> varies a lot!

# In[ ]:


df.info()


# -> We can see the columns with lots of null values.
# 
# -> Some data types also don't make sense:  PassengerId, Survived, and Pclass do not have numerical value, so the numbers are not really meant to be integers.

# <table class="table table-striped">
#   <thead>
#     <tr>
#       <th>Pandas Type</th>
#       <th>Native Python Type</th>
#       <th>Description</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <td>object</td>
#       <td>string</td>
#       <td>The most general dtype. Will be assigned to your column if column has mixed types (numbers and strings).</td>
#     </tr>
#     <tr>
#       <td>int64</td>
#       <td>int</td>
#       <td>Numeric characters. 64 refers to the memory allocated to hold this character.</td>
#     </tr>
#     <tr>
#       <td>float64</td>
#       <td>float</td>
#       <td>Numeric characters with decimals. If a column contains numbers and NaNs (see below), pandas will default to float64, in case your missing value has a decimal.</td>
#     </tr>
#     <tr>
#       <td>datetime64, timedelta[ns]</td>
#       <td>N/A (but see the <a href="http://doc.python.org/2/library/datetime.html">datetime</a> module in Python’s standard library)</td>
#       <td>Values meant to hold time data. Look into these for time series experiments.</td>
#     </tr>
#   </tbody>
# </table>

# Let's change a column's datatype from int to string (which becomes an object to pandas):

# In[4]:


df['Survived'].astype(str)


# In[ ]:


df.info()


# Whoops!  The astype function returned a view, but it didn't change the underlying dataframe.  To do that, we need to explicitly assign the returned dataframe column back into the `df['Survived']` column.

# In[5]:


df['Survived'] = df['Survived'].astype(str)


# In[6]:


df.info()


# In[ ]:


# Change the other two columns too
df['PassengerId'] = df['PassengerId'].astype(str)
df['Pclass'] = df['Pclass'].astype(str)


# ## Visualization
# 
# Now for some fun stuff.  Let's try to make some simple plots to see what observations we can make.

# In[ ]:


df['Fare']


# In[ ]:


df['Fare'].plot()


# This shows Index vs Fare, i.e., what the value of every Fare was.  We can get a sense of what all the fares were from this, but really we probably want to see a distribution of values.

# In[7]:


df['Fare'].plot(kind='hist')


# It looks like there are a bunch of low cost tickets, or maybe just a few very *very* expensive tickets.
# 
# **Our first look at potentially suspicious values:**  Are there any 0 values?

# In[ ]:


df.loc[df['Fare']==0]


# A brief search of some names shows that Mr Lionel Leonard, William Cahoone Johnson Jr., Alfred Johnson, and William Henry Tornquist were American Line employees.  It may make sense that they would have traveled on complementary fare.
# 
# ... more investigation may be warranted.
# 
# But let's looks at the columns that have 'NaN'.

# In[ ]:


df.isna()


# In[ ]:


df.isna().sum()


# In[ ]:


df.shape


# In[ ]:


df.isna().sum() / df.shape[0]


# * 20% of age data is missing
# * 77% of cabin data is missing
# * 0.2% of embarked data is missing

# If we want to use those data columns, we would potentially stop here and try to figure out how we need/want to deal with the values that are missing.
# 
# Let's see how Age is related to Survived.
# 
# *Warning: I'm going to start with some inconvenient plots... just because that's exploratory work for ya.*

# In[ ]:


df.groupby('Survived').plot(kind='box',y='Age');


# In[ ]:


df.groupby('Survived').boxplot(column='Age',subplots=False)


# In[ ]:


df.boxplot(column='Age',by='Survived')


# In[ ]:


numcols = ['Age','SibSp','Parch','Fare']

#for i in numcols:
df.groupby('Survived').boxplot(column=numcols,subplots=False)
df.boxplot(column=numcols,by='Survived')


# In[ ]:


df.plot(kind='hist',x='Age',y='Survived')


# In[ ]:


df.groupby('Survived')['Age'].value_counts()


# In[ ]:





# In[ ]:





# **OK**.  Let's pause and re-group.
# 
# Here are the variables we might like to look at:
# * `df.loc[df['Survived'] == '0', 'Age']`: the Age values of those who did not survive
# * `df.loc[df['Survived'] == '1', 'Age']`: the Age values of those who did survive
# 
# Let's use matplotlib to do a histogram of these.

# In[ ]:


a = df.loc[df['Survived'] == '0', 'Age']
plt.hist(a);


# That's a little more straight-forward.

# In[ ]:


fig,ax = plt.subplots(2,1)

a = df.loc[df['Survived'] == '0', 'Age']
b = df.loc[df['Survived'] == '1', 'Age']

a.plot.hist(ax=ax[0],width=5)
b.plot.hist(ax=ax[1],width=5)


# And it would be nice to plot the bars next to each other too to directly compare them.

# In[ ]:


a = df.loc[df['Survived'] == '0', 'Age']
b = df.loc[df['Survived'] == '1', 'Age']
plt.hist([a,b]);


# In[ ]:


a = df.loc[(df['Survived'] == '0') & (df['Age'] > 18), 'Age']
b = df.loc[(df['Survived'] == '1') & (df['Age'] > 18), 'Age']
plt.hist([a,b]);


# In[ ]:


a = df.loc[(df['Survived'] == '0') & (df['Age'] < 18), 'Age']
b = df.loc[(df['Survived'] == '1') & (df['Age'] < 18), 'Age']
plt.hist([a,b]);


# Now that we have a method down for Age, let's apply it to other variables: Sex, Fare, and Pclass.

# In[ ]:


a = df.loc[df['Survived'] == '0', 'Sex']
b = df.loc[df['Survived'] == '1', 'Sex']
plt.hist([a,b]);


# In[ ]:


a = df.loc[df['Survived'] == '0', 'Fare']
b = df.loc[df['Survived'] == '1', 'Fare']
plt.hist([a,b]);


# Sometimes the scales for some values (like the large values here near 0) might make it hard to get a good comparison at other values (like the smaller values for 200+).

# In[ ]:


a = df.loc[(df['Survived'] == '0') & (df['Fare'] > 50), 'Fare']
b = df.loc[(df['Survived'] == '1') & (df['Fare'] > 50), 'Fare']
plt.hist([a,b]);


# In[ ]:


a = df.loc[(df['Survived'] == '0') & (df['Fare'] < 50), 'Fare']
b = df.loc[(df['Survived'] == '1') & (df['Fare'] < 50), 'Fare']
plt.hist([a,b]);


# In this dataset, 'Pclass' also acts as an indicator for socio-economic status.

# In[ ]:


a = df.loc[df['Survived'] == '0', 'Pclass']
b = df.loc[df['Survived'] == '1', 'Pclass']
plt.hist([a,b]);

