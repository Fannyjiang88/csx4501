#!/usr/bin/env python
# coding: utf-8

# ## Interacting with external data -- our own pre-class survey

# ## Import the modules

# In[ ]:


import sqlite3
import pandas as pd


# ## Get the data

# In[ ]:


surveylink = 'https://docs.google.com/spreadsheets/d/13P5Q87XroFROfvieaywwsnWwBUNOUGBbDT6g3UlM6xM/export?format=csv'


# In[ ]:


df = pd.read_csv(surveylink)


# ## Look at the data

# In[ ]:


df


# In[ ]:


for row in df.index:
    print(df.iloc[row][1:].values)


# ## Put the data into a database file

# In[ ]:


connectionPreworkshop = sqlite3.connect('preworkshop.db')


# In[ ]:


cursorPreworkshop = connectionPreworkshop.cursor()


# In[ ]:


cursorPreworkshop.execute('''
CREATE TABLE preworkshop (sql text,
                        python text,
                        jupyter text,
                        pandas text);
''')


# In[ ]:


for row in df.index:
    answers = df.iloc[row][1:].values
    cursorPreworkshop.execute('''INSERT INTO preworkshop (sql, python, jupyter, pandas) 
            VALUES (?,?,?,?);''', answers)


# In[ ]:


connectionPreworkshop.commit()


# ## Run a query to check the data is there

# In[ ]:


df = pd.read_sql_query('select * from preworkshop',connectionPreworkshop)


# In[ ]:


df


# ## Make a plot of the data

# In[ ]:


df['pandas'].value_counts().plot.pie()


# ## Create a new table in the database
# 
# This table will allow us create a numerical 'mastery' score.

# In[ ]:


cursorPreworkshop.execute('''
CREATE TABLE answers (answerText text,
                        answerCode integer);
''')


# In[ ]:


answers = [
    ['Use it all the time',4],
    ['Use them all the time',4],
    ['Not an expert, but comfortable with reading commands',3],
    ['Not an expert, but comfortable with running them',3],
    ['Familiar with it but could use a refresher',2],
    ['Familiar with them but could use a refresher',2],
    ['Not at all',1],
    ['What\'s Pandas?',0],
]

for i in answers:
    cursorPreworkshop.execute('''INSERT INTO answers (answerText, answerCode) 
            VALUES (?,?);''', i)


# In[ ]:


connectionPreworkshop.commit()


# ## Look at the table

# In[ ]:


df = pd.read_sql_query('select * from answers',connectionPreworkshop)


# In[ ]:


df


# ## Create a new column in the dataframe for mastery score

# In[ ]:


df = pd.read_sql_query('''
select a1.answerCode as sql, 
    a2.answerCode as python, 
    a3.answerCode as jupyter, 
    a4.answerCode as pandas,
    (a1.answerCode + a2.answerCode + a3.answerCode + a4.answerCode)/16. as Mastery
from preworkshop p
join answers a1
on p.sql = a1.answerText
join answers a2
on p.python = a2.answerText
join answers a3
on p.jupyter = a3.answerText
join answers a4
on p.pandas = a4.answerText
''',connectionPreworkshop)


# In[ ]:


df


# ## Plot the data

# In[ ]:


df['Mastery'].plot.hist(range=(0.0,1.0),bins=20)

