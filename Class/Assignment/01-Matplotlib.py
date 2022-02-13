#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:ea26706d-ace5-4b14-b029-40cb5f0a291c.png)

# ## Let's start by getting some data and doing some Python review

# In[ ]:


# This opens the file and puts the text of the "I Have a Dream" speech into the 'speech' variable

with open('i-have-a-dream.txt','r') as f:
    speech = f.read()


# In[ ]:


speech


# In[ ]:


speech.index('I have a dream')


# In[ ]:


speech[5768:5768+34]


# In[ ]:


dir(speech)


# In[ ]:


help(speech.count)


# In[ ]:


speech.count('I have a dream')


# In[ ]:


help(speech.index)


# In[ ]:


speech.index('I have a dream',0)


# In[ ]:


speech.index('I have a dream',5768+1)


# In[ ]:


dreamstring = 'I have a dream'
numdreams = speech.count(dreamstring)
startindex = 0

for i in range(numdreams):

    # find where 'I have a dream starts'
    startindex = speech.index('I have a dream',startindex)
    
    # find the end of the sentence after the phrase
    endindex = speech.index('.',startindex)
    
    print(speech[startindex:endindex+1] + '\n')
    
    # we reset startindex so that the next time through the loop,
    # we find the next occurrence of the phrase
    startindex = endindex


# ## Finding the number of times each word occurs

# We should get rid of the punctuation.  (We don't want to count "dream" and "dream," as two different strings)

# In[ ]:


specialchars = '.,-!:'

# remove each character in the specialchars string
# "replace" is a string method that replaces the first argument with the second argument

for c in specialchars:
    speech = speech.replace(c,' ')


# Just to be safe, we'll also make everything lower case, so that "Dream" and "dream" count as the same word for counting purposes.

# In[ ]:


speech = speech.lower()


# We now create a dictionary, and for each word, we start counting the number of times it occurs.
# 
# The dictionary `speechwordcount` has all the words as keys, and for each word, the value is the number of times it occurs.

# In[ ]:


speechwordcount = {}
speechwords = speech.split(' ')
for c in speechwords:
    if c in speechwordcount.keys():
        speechwordcount[c] += 1
    else:
        speechwordcount[c] = 1


# In[ ]:


speechwordcount


# We want to see which words occur most frequently.

# In[ ]:


sorted(speechwordcount)


# That didn't do the trick.  It sorted the keys alphabetically....
# 
# The below cell shows how to sort by values, but don't worry about the specifics for the moment.  This is only to generate the data so we can plot it.

# In[ ]:


sortspeechcount = {k: v for k, v in sorted(speechwordcount.items(), key=lambda item: -item[1])}
sortspeechcount


# ## Now let's jump into some plotting with matplotlib!

# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


countvals = sortspeechcount.values()


# In[ ]:


print(countvals)


# In[ ]:


plt.plot(countvals)


# In[ ]:


# This will give an error!
plt.plot(countvals[6:])


# Recall that we have to be careful when indexing data related to dictionaries.

# We can explicitly "cast" some variables as the type we want, when it's a valid operation

# In[ ]:


type(countvals)


# In[ ]:


countvalslist = list(countvals)


# In[ ]:


type(countvalslist)


# In[ ]:


plt.plot(countvalslist[6:])


# We can numerically index a list -- let's do it for both words and word counts.

# In[ ]:


frequentwords = list(sortspeechcount.keys())[6:31]
frequentvals = list(sortspeechcount.values())[6:31]


# In[ ]:


plt.plot(frequentwords,frequentvals)


# Just so you see it, there are two main ways to create plots in matplotlib
# 
# 1. Use matplotlib.pyplot (which here is aliased as plt) -- this is the higher-level and easier to use module
# 2. Use figure and axes objects (objects in the object-oriented programming sense) to manipulate the graphical object you see

# In[ ]:


x = [1, 2, 3, 4]
y = [10, 11, 12, 13]


# In[ ]:


plt.plot(x,y)


# In[ ]:


plt.bar(x,y)


# In[ ]:


plt.bar(x,y,color='r')


# In[ ]:


# the object way
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y)


# In[ ]:


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(x,y)


# In[ ]:


fig,ax = plt.subplots(1,2,figsize=(8,4))

x = [1,2,3,4]
y1 = [1,2,3,4]
y2 = [1,4,9,16]

ax[0].plot(x,y1)
ax[1].plot(x,y2,color='blue', linestyle='--', linewidth=2)

plt.show()


# Let's stick with plt for the moment (and later we'll migrate to pandas)

# In[ ]:


plt.figure(figsize=(12,5))
plt.plot(frequentwords,frequentvals)


# In[ ]:


plt.figure(figsize=(12,5))
plt.bar(frequentwords,frequentvals)


# In[ ]:


plt.figure(figsize=(12,5))
plt.barh(frequentwords,frequentvals)


# In[ ]:


barcolors = []
for i in frequentwords:
    # could be:
    # if i == 'i' or i == 'have' or i == 'dream'
    # or could be:
    if i in ['i','have','a','dream']:
        barcolors.append('blue')
    else:
        barcolors.append('grey')
barcolors


# In[ ]:


plt.figure(figsize=(12,5))
plt.barh(frequentwords,frequentvals,color=barcolors)


# In[ ]:


plt.figure(figsize=(12,5))
plt.barh(frequentwords,frequentvals,color=barcolors)
plt.xlim([10.8,15])


# In[ ]:


plt.figure(figsize=(12,5))
plt.barh(frequentwords,frequentvals,color=barcolors)
plt.xlim([10.8,15])
plt.text(12,
         20,
         '"I" is said 20 times more frequently than "dream"!!!.... wait... what???',
         fontsize=13);


# In[ ]:


plt.figure(figsize=(12,5))
plt.pie(frequentvals, labels = frequentwords);

