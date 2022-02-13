#!/usr/bin/env python
# coding: utf-8

# ## The essentials of establishing connections and executing SQL statements via Python

# Import the libraries we are going to use

# In[ ]:


import sqlite3
import pandas as pd


# Establish the connection object to the database

# In[ ]:


conn = sqlite3.connect('survey.db')


# Establish the cursor object for executing queries

# In[ ]:


cur = conn.cursor()


# Execute a query with the cursor

# In[ ]:


cur.execute("SELECT * FROM Person;")


# Retrieve results

# In[ ]:


cur.fetchall()


# Close things down

# In[ ]:


cur.close()
conn.close()


# Right from the start, it's useful to use Pandas and dataframes

# In[ ]:


conn = sqlite3.connect('survey.db')
cur = conn.cursor()
query = 'SELECT * FROM Person;'
pd.read_sql_query(query,conn)


# This is a wrapper function that uses the cursor to execute a query, and then prints the results

# In[ ]:


def run_query_cursor(query):
    cur.execute(query)
    for i in cur.fetchall():
        print(i)


# This is another wrapper that instead uses Pandas

# In[ ]:


def run_query_pd(query):
    return pd.read_sql_query(query,conn)


# ## Here are the tables we have in the database

# In[ ]:


run_query_pd('select name from sqlite_master;')


# In[ ]:


query = '''
SELECT *
FROM person;
'''
run_query_cursor(query)


# In[ ]:


query = '''
SELECT *
FROM person;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM site;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM visited;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM survey;
'''
run_query_pd(query)


# # SELECT

# In[ ]:


query = '''
SELECT family, personal
FROM person;
'''
run_query_pd(query)


# In[ ]:


query = '''
seLEcT FamiLY, PERSONal
from perSON;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT personal, id, family, family, id, personal
FROM person;
'''
run_query_pd(query)


# In[ ]:


# Write a query that selects only the 'name' from the 'Site' table
query = '''

'''
run_query_pd(query)


# # dealing with duplicates and sorting

# In[ ]:


query = '''
SELECT quant
FROM survey;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant
FROM survey;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant, taken
FROM survey;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant, taken
FROM survey
ORDER BY quant;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant, taken
FROM survey
ORDER BY quant, taken DESC;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM person
ORDER BY id;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM person
ORDER BY id DESC;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant, person
FROM survey
ORDER BY quant ASC;
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT quant, person
FROM survey
ORDER BY quant ASC, person;
'''
run_query_pd(query)


# In[ ]:


# Write a query that selects the distinct dates shown in the 'Visited' table
query = '''

'''
run_query_pd(query)


# In[ ]:


# Write a query that shows the full names of scientists in the 'Person' table, ordered by family name
query = '''

'''
run_query_pd(query)


# # Filtering
# Selecting records that match certain criteria

# In[ ]:


query = '''
SELECT *
FROM visited
WHERE site = 'DR-1';
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT id
FROM visited
WHERE site = 'DR-1';
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM visited
WHERE (site = 'DR-1') AND (dated < '1930-01-01');
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM survey
WHERE (person = 'lake') OR (person = 'roe');
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM survey
WHERE person IN ('lake','roe');
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM survey
WHERE quant = 'sal' AND person = 'lake' OR person = 'roe';
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM survey
WHERE quant = 'sal' AND (person = 'lake' OR person = 'roe');
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT *
FROM visited
WHERE site LIKE 'DR%';
'''
run_query_pd(query)


# In[ ]:


query = '''
SELECT DISTINCT person, quant
FROM survey
WHERE person = 'lake' OR person = 'roe';
'''
run_query_pd(query)


# In[ ]:


# Say we want all sites that lie within 48 degrees of the equator, that is, latitutide from -48 to 48
# Fix this:
query = '''
SELECT *
FROM site
WHERE (lat > -48) OR (lat < 48);
'''
run_query_pd(query)


# In[ ]:


# Normalized salinity reading should be between 0.0 and 1.0.  
# Select records from the 'Survey' table that are outside this range:
query = '''

'''
run_query_pd(query)


# # calculating new values

# In[ ]:


# Perhaps 'roe' was misreporting salinity values
query = '''
SELECT *
FROM survey
WHERE quant = 'sal'
ORDER BY person DESC;
'''
run_query_pd(query)


# In[ ]:


# We can divide by 100 but ....
query = '''
SELECT person, quant, reading/100.0
FROM survey
WHERE quant = 'sal'
ORDER BY person DESC;
'''
run_query_pd(query)


# In[ ]:


# slight detour
query = '''
SELECT 1.05*reading
FROM survey
WHERE quant = 'rad';
'''
run_query_pd(query)


# In[ ]:


# slight detour
query = '''
SELECT 1.05*reading AS 'Radiation corrected by 5%'
FROM survey
WHERE quant = 'rad';
'''
run_query_pd(query)


# In[ ]:


# temperature in Fahrenheit
query = '''
SELECT reading
FROM survey
WHERE quant = 'temp';
'''
run_query_pd(query)


# In[ ]:


# temperature in Celsius
query = '''
SELECT round(5 * (reading - 32) / 9, 2) as 'Temp (C)'
FROM survey
WHERE quant = 'temp';
'''
run_query_pd(query)


# In[ ]:


# String concatenation
query = '''
SELECT personal || ' ' || family
FROM person;
'''
run_query_pd(query)


# In[ ]:


# back to salinity
# We can divide by 100 for 'roe' ....
query = '''
SELECT person, quant, reading/100.0
FROM survey
WHERE quant = 'sal' AND person = 'roe';
'''
run_query_pd(query)


# In[ ]:


# combine this now with the notion of unions
query = '''
SELECT *
FROM person
WHERE id = 'dyer'
UNION
SELECT *
FROM person
WHERE id = 'roe';
'''
run_query_pd(query)


# In[ ]:


# UNION vs UNION ALL
query = '''
SELECT *
FROM person
WHERE id = 'dyer'
UNION ALL
SELECT *
FROM person;
'''
run_query_pd(query)


# In[ ]:


# Use UNION to show the salinity/100 for 'roe' and original salinity readings for everyone else
query = '''

'''
run_query_pd(query)


# ## Let's use Python to follow through with the whole process inside a function

# In[ ]:


person_id = 'roe'
# For later, b = "roe'; DROP TABLE Survey; SELECT '"

a = "SELECT personal || ' ' || family FROM Person WHERE id='"
b = person_id
c = "';" 
mystring = a + b + c
print(mystring)


# In[ ]:


# how we can execute a query from a python function
def get_name(database_file, person_id):
    query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"    
    
    c = sqlite3.connect(database_file)
    cursor = c.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    c.close()
    
    return results
    #return results[0][0]

print(get_name('survey.db','roe'))


# ## Pitfalls

# In[ ]:


# SQL INJECTION
def get_name(database_file, person_id):
    query = "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"    
    
    c = sqlite3.connect(database_file)
    cursor = c.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    c.close()
    
    return results[0][0]

# UH-OH:
# print(get_name('survey.db',"roe'; DROP TABLE Survey; SELECT '"))


# In[ ]:


# PREVENT SQL INJECTION
def get_name(database_file, person_id):
    query = "SELECT personal || ' ' || family FROM Person WHERE id=?;"   
    
    c = sqlite3.connect(database_file)
    cursor = c.cursor()
    cursor.execute(query, [person_id])
    results = cursor.fetchall()
    cursor.close()
    c.close()
    
    return results[0][0]

print(get_name('survey.db','roe'))
# UH-OH?
# print(get_name('survey.db',"roe'; DROP TABLE Survey; SELECT '"))


# ## Altering data in the database

# In[ ]:


# Example table modification
def add_name(database_file, new_person):
    query = "INSERT INTO Person (id, personal, family) VALUES (?, ?, ?);"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, list(new_person))
    cursor.close()
    connection.close()

# Insert a new name
add_name('survey.db', ('barrett', 'Mary', 'Barrett'))
# Check it exists
print("Full name for barrett:", get_name('survey.db', 'barrett'))


# In[ ]:


# Example table modification
# must do the commit!
def add_name(database_file, new_person):
    query = "INSERT INTO Person (id, personal, family) VALUES (?, ?, ?);"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, list(new_person))
    cursor.close()
    connection.commit()
    connection.close()

# Insert a new name
add_name('survey.db', ('barrett', 'Mary', 'Barrett'))
# Check it exists
print("Full name for barrett:", get_name('survey.db', 'barrett'))


# In[ ]:


# The database that we are originally connected to reflects the change
query = '''
SELECT *
FROM person;
'''
run_query_pd(query)

