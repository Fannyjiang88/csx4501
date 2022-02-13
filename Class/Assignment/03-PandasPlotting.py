#!/usr/bin/env python
# coding: utf-8

# # Now for the Pandas plotting!

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt


# Let's start off with plotting the Anscombe's data I showed at the very beginning.

# In[ ]:


df = pd.read_csv('anscombe.csv')


# In[ ]:


df


# We can use indexing with `loc` to look at just dataset I.

# In[ ]:


a = df.loc[df['dataset'] == 'I']


# In[ ]:


a


# In[ ]:


a.plot(x='x', y='y')


# What's with the zig-zags?
# 
# The default is to do a line plot connecting the points, and since the points are plotted out of numerical order, the connecting lines zigs back and forth in the x and y direction.

# We actually want to plot this as a scatter plot instead of a line plot.

# In[ ]:


a.plot(kind='scatter', x='x', y='y')


# The `kind` parameter makes it very easy to make a variety of different elementary plots:
# 
# * `line` : line plot
# * `bar` : vertical bar plot
# * `barh` : horizontal bar plot
# * `hist` : histogram
# * `box` : boxplot
# * `kde` : kernel density estimation plot
# * `density` : same as kde
# * `area` : area plot
# * `pie` : pie plot
# * `scatter` : scatter plot
# * `hexbin` : hexbin plot

# In[ ]:


a.plot(kind='bar', x='x', y='y')


# Note that pandas does not necessarily try to order the x-axis here for us.

# In[ ]:


a


# In[ ]:


a.sort_values(by='x')


# In[ ]:


a.sort_values(by='x').plot()


# In[ ]:


a.sort_values(by='x').plot(kind='bar', x='x', y='y')


# And if we try to plot the whole dataframe?

# In[ ]:


df.plot(kind='bar', x='x', y='y')


# It can be useful to group the dataframe by common values in a certain column.
# 
# Here it would be useful to generate a plot for each of the different values contained in the `dataset` column.
# 
# We can do this with `groupby`.

# In[ ]:


df.groupby('dataset').plot(kind='bar', x='x', y='y')


# In[ ]:


df.groupby('dataset').plot(kind='scatter', x='x', y='y')


# `groupby` is useful as well for doing analysis broken down by subgroups within the dataframe.

# In[ ]:


df.groupby('dataset').count()


# And the grouping can be used to analyze just a single column

# In[ ]:


df.groupby('dataset')['x'].count()


# There are several aggregate functions that can provide useful summary info when used with the `groupby`

# In[ ]:


df.groupby('dataset')[['x','y']].mean()


# The aggregate functions can get applied via the `agg` method.  `agg(Mean='mean')` implies that the `mean` function will get applied to the subgroups, and the resulting column that is return will have a label of `Mean`

# In[ ]:


df.groupby('dataset')['x'].agg(Mean='mean')


# In[ ]:


df.groupby('dataset').agg(MeanX=('x','mean'),MeanY=('y','mean'),
                          StdX=('x','std'),StdY=('y','std'))


# # Dream Speech

# Let's return to the Dream speech and put the data into a dataframe.

# In[ ]:


df = pd.read_csv('dreamspeechpd.csv')


# In[ ]:


df


# It is easy to use pandas to generate a plot

# In[ ]:


df.plot()


# And to label the x-axis by the word column... though here that's not terribly useful

# In[ ]:


df.plot(x='word')


# In[ ]:


df.plot(kind='bar', x='word')


# That x-axis gets swamped, and really we may only be interested in the first 30 words or so.  Let's narrow down the range.

# In[ ]:


df.iloc[:30].plot(kind='bar', x='word')


# We can make the horizontal bar plot to make the words easier to read.

# In[ ]:


df.iloc[:30].plot(kind='barh', x='word')


# By the way, you can include extra spaces and return characters inside a function's list of arguments.  This can make things cleaner and easier to read.

# In[ ]:


df.iloc[:30].plot(kind='barh',
                  x='word')


# We'll improve the look by increasing figure size.

# In[ ]:


df.iloc[:30].plot(kind='barh',
                  x='word',
                  figsize=(12,5))


# Let's highlight the bars for the words in "I Have a Dream".  To do that, we generate a list of color-words that are all 'grey' with the exception of being 'blue' in the locations of the target words.

# In[ ]:


barcolors = []
for i in df[:30].index:
    if df.loc[i,'word'] in ['i','have','a','dream']:
        barcolors.append('blue')
    else:
        barcolors.append('grey')
print(barcolors)


# In[ ]:


df.iloc[:30].plot(kind='barh',
                  x='word',
                  figsize=(12,5),
                  color=barcolors)


# This didn't work!
# 
# 1. You have to be careful and very detailed while plotting.  Data viz can be very fun work but also the source of hours of headache.

# In[ ]:


df[:30].plot(kind='barh',
             x='word',
             y='count',   # <------ this line has to be included
             figsize=(12,5),
             color=barcolors)


# 2. While Pandas makes plotting easy, you may find that you need the lower-level control of Matplotlib if you really want to get more control over the aesthetics.
# 
# And... you can use both of them together!!

# In[ ]:


ax = df.iloc[:30].plot(kind='barh',
                       x='word',
                       y='count',
                       figsize=(12,5),
                       color=barcolors)

ax.legend(['Word counts of MLK speech'])


# ## Finally, tweak some fontsizes, make some axis labels, and SAVE the figure in a file

# In[ ]:


plt.rcParams['font.size'] = '12'

ax = df.iloc[:30].plot(kind='barh',
                       x='word',
                       y='count',
                       figsize=(12,6),
                       color=barcolors)

ax.legend(['Word counts of MLK speech'])
ax.set_title('Word Counts of "I Have a Dream"')
ax.set_xlabel('Word Counts',fontsize=14)
ax.set_ylabel('Word',fontsize=14)

ax.figure.savefig('dreamcount.png')


# Look for the new 'dreamcount.png' file in your directory.

# # Bonus: other libraries

# We will cover more data viz next week, but here is a teaser of using Seaborn, and of making a wordcloud.

# In[ ]:


import seaborn as sns


# In[ ]:


df = pd.read_csv('anscombe.csv')


# In[ ]:


# Show the results of a linear regression within each dataset
sns.lmplot(data=df, x="x", y="y",
           col="dataset", hue="dataset");


# In[ ]:


from wordcloud import WordCloud


# In[ ]:


with open('i-have-a-dream.txt','r') as f:
    speech = f.read()


# In[ ]:


wordcloud = WordCloud().generate(speech)

# Display the generated image:
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation='bilinear')

