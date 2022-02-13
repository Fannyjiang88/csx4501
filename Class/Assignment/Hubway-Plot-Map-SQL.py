#!/usr/bin/env python
# coding: utf-8

# # SQL + Pandas Plotting
# This notebook is taken in part from a [Dataquest intro](https://www.dataquest.io/blog/sql-basics/).

# In[ ]:


# Grab the database
get_ipython().system("wget 'https://dataquest.io/blog/large_files/hubway.db'")


# In[ ]:


import sqlite3
import pandas as pd
db = sqlite3.connect('hubway.db')
def run_query(query):
    return pd.read_sql_query(query,db)


# In[ ]:


run_query('SELECT name FROM sqlite_master;')


# The `trips` table:
# * id — A unique integer that serves as a reference for each trip
# * duration — The duration of the trip, measured in seconds
# * start_date — The date and time the trip began
# * start_station — An integer that corresponds to the id column in the stations table for the station the trip started at
# * end_date — The date and time the trip ended
# * end_station — The 'id' of the station the trip ended at
# * bike_number — Hubway's unique identifier for the bike used on the trip
# * sub_type — The subscription type of the user. "Registered" for users with a membership, "Casual" for users without a membership
# * zip_code — The zip code of the user (only available for registered members)
# * birth_date — The birth year of the user (only available for registered members)
# * gender — The gender of the user (only available for registered members)
# 
# The `stations` table:
# * id — A unique identifier for each station (corresponds to the start_station and end_station columns in the trips table)
# * station — The station name
# * municipality — The municipality that the station is in (Boston, Brookline, Cambridge or Somerville)
# * lat — The latitude of the station
# * lng — The longitude of the station

# In[ ]:


run_query('SELECT * FROM trips LIMIT 5;')


# In[ ]:


run_query('SELECT * FROM stations LIMIT 5;')


# Let's say that we want to answer the following questions:
# * What was the duration of the longest trip?
# * How many trips were taken by 'registered' users?
# * What was the average trip duration?
# * Do registered or casual users take longer trips?
# * Which bike was used for the most trips?
# * What is the average duration of trips by users over the age of 30?

# In[ ]:


query = 'SELECT * FROM trips LIMIT 5;'
run_query(query)


# In[ ]:


query = 'SELECT duration, start_date FROM trips LIMIT 5'
run_query(query)


# In[ ]:


query = 'SELECT count(*) FROM trips'
run_query(query)


# In[ ]:


query = 'SELECT count(*) FROM trips WHERE start_date > "2012-01-01" and start_date < "2013-01-01"'
run_query(query)


# ### What was the duration of the longest trip?

# In[ ]:


query = '''
SELECT duration FROM trips
ORDER BY duration DESC
LIMIT 1;
'''
run_query(query)


# In[ ]:


query = '''
SELECT duration
FROM trips
ORDER BY duration DESC
LIMIT 10
'''
run_query(query)


# In[ ]:


query = '''
SELECT * FROM trips
WHERE duration > 9990;
'''
run_query(query)


# In[ ]:


query = '''
SELECT * FROM trips
WHERE (duration >= 9990) AND (sub_type = "Registered")
ORDER BY duration DESC;
'''
run_query(query)


# ### How many trips were taken by 'registered' users?

# In[ ]:


query = '''
SELECT COUNT(*)
FROM trips
WHERE sub_type = "Registered";
'''
run_query(query)


# In[ ]:


query = '''
SELECT COUNT(*) AS "Total Trips by Registered Users"
FROM trips
WHERE sub_type = "Registered";
'''
run_query(query)


# ### What was the average trip duration?

# In[ ]:


query = '''
SELECT AVG(duration) AS "Average Duration"
FROM trips;
'''
run_query(query)


# ### Do registered or casual users take longer trips?

# In[ ]:


query = '''
SELECT sub_type, AVG(duration) AS "Average Duration"
FROM trips
GROUP BY sub_type;
'''
run_query(query)


# ### Which bike was used for the most trips?

# In[ ]:


query = '''
SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
LIMIT 1;
'''
run_query(query)


# ### What is the average duration of trips by users over the age of 30?

# In[ ]:


query = '''
SELECT AVG(duration) FROM trips
WHERE (2020 - birth_date) > 30;
'''
run_query(query)


# In[ ]:


query = '''
SELECT * FROM stations
LIMIT 5;
'''
run_query(query)


# ### Illustrate JOIN to get stations with the most round trips

# In[ ]:


query = '''
SELECT stations.station AS "Station", COUNT(*) AS "Count"
FROM trips 
INNER JOIN stations
ON trips.start_station = stations.id
GROUP BY stations.station
ORDER BY COUNT(*) DESC
LIMIT 5;
'''
run_query(query)


# In[ ]:


query = '''
SELECT stations.station AS "Station", COUNT(*) AS "Count"
FROM trips 
INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY stations.station
ORDER BY COUNT(*) DESC
LIMIT 5;
'''
run_query(query)


# In[ ]:


query = '''
SELECT COUNT(trips.id) AS "Count"
FROM trips 
INNER JOIN stations AS start
ON trips.start_station = start.id
INNER JOIN stations AS end
ON trips.end_station = end.id
WHERE start.municipality <> end.municipality;
'''
run_query(query)


# # Now to tackle some plotting
# 
# * How many trips incurred additional fees (lasted longer than 30 minutes)?
# * Which bike was used for the longest total time?
# * Did registered or casual users take more round trips?
# * Which municipality had the longest average duration?

# In[ ]:


# Wait for me to run this -- example of memory issues
df = pd.read_sql_query("SELECT * FROM trips;", db)
df
# df = pd.read_sql_query("select * from trips WHERE start_date < '2012-01-01';", db)
#query = 'SELECT count(*) FROM trips WHERE start_date > "2012-01-01" and start_date < "2013-01-01"'
#run_query(query)


# In[ ]:


import sqlite3
import pandas as pd
import folium
from folium import plugins
db = sqlite3.connect('hubway.db')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df = pd.read_sql_query('''
SELECT *
FROM stations
''',db)
df


# ## First, perhaps let's actually "look" at the data spatially

# In[ ]:


stops_map = folium.Map(location=[42.34,-71.10], zoom_start=11)
stops_map


# In[ ]:


stops_map = folium.Map(location=[42.34,-71.10], zoom_start=12)

marker_cluster = folium.plugins.MarkerCluster().add_to(stops_map)
for name, row in df.iterrows():
    folium.Marker([row["lat"], row["lng"]], popup=row["station"]).add_to(marker_cluster)

stops_map


# In[ ]:


[[row["lat"], row["lng"]] for name, row in df.iterrows()]


# In[ ]:


stops_heatmap = folium.Map(location=[42.34,-71.10], zoom_start=14)

stops_heatmap.add_child(folium.plugins.HeatMap([[row["lat"], row["lng"]]
                                                   for name, row in df.iterrows()]))

stops_heatmap


# In[ ]:


df = pd.read_sql_query('''
SELECT MAX(lat), MIN(lat), MAX(lng), MIN(lng)
FROM stations
''',db)
df


# In[ ]:


df = pd.read_sql_query('''
SELECT (MAX(lat)+MIN(lat))/2 as centerLat, (MAX(lng)+MIN(lng))/2 as centerLng
FROM stations
''',db)
df


# In[ ]:


centerLat = df.loc[0,'centerLat']
centerLng = df.loc[0,'centerLng']


# In[ ]:


df = pd.read_sql_query('''
SELECT *
FROM stations
''',db)

stops_heatmap = folium.Map(location=[centerLat,centerLng], zoom_start=13)
stops_heatmap.add_child(folium.plugins.HeatMap([[row["lat"], row["lng"]]
                                                   for name, row in df.iterrows()]))

stops_heatmap


# In[ ]:


df = pd.read_sql_query('''
SELECT stations.station AS "Station", COUNT(*) AS "Count"
FROM trips 
INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY stations.station
ORDER BY COUNT(*) DESC;
''', db)


# In[ ]:


df


# In[ ]:


df = pd.read_sql_query('''
SELECT stations.station AS "Station", COUNT(*) AS "Count", stations.lat, stations.lng
FROM trips 
INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY stations.station
ORDER BY COUNT(*) DESC;
''', db)


# In[ ]:


df


# In[ ]:


stops_heatmap = folium.Map(location=[centerLat,centerLng], zoom_start=13)
stops_heatmap.add_child(folium.plugins.HeatMap([[row["lat"], row["lng"], row["Count"]]
                                                   for name, row in df.iterrows()]))

stops_heatmap


# In[ ]:


marker_cluster = folium.plugins.MarkerCluster().add_to(stops_heatmap)
for name, row in df.iterrows():
    folium.Marker([row["lat"], row["lng"]], popup=row["Count"]).add_to(marker_cluster)

stops_heatmap


# In[ ]:


df[:20].plot.barh(x='Station',y='Count')


# In[ ]:


df.sort_values("Count",ascending=True)[-20:].plot.barh(x='Station',y='Count')


# In[ ]:


df2 = df.sort_values("Count",ascending=True)[-20:]
stops_heatmap = folium.Map(location=[centerLat,centerLng], zoom_start=13)
stops_heatmap.add_child(folium.plugins.HeatMap([[row["lat"], row["lng"], row["Count"]]
                                                   for name, row in df2.iterrows()]))

marker_cluster = folium.plugins.MarkerCluster().add_to(stops_heatmap)
for name, row in df2.iterrows():
    folium.Marker([row["lat"], row["lng"]], popup=row["Count"]).add_to(marker_cluster)

stops_heatmap


# In[ ]:


stops_heatmap.save('stops.html')


# In[ ]:


df = pd.read_sql_query('''
SELECT duration
FROM trips;
''', db)


# In[ ]:


df2 = df.copy()


# In[ ]:


df[['duration']].hist()


# In[ ]:


df.hist(bins=100)


# In[ ]:


pd.read_sql_query('''
SELECT count(*)
FROM trips
WHERE duration > 30*60;
''', db)


# In[ ]:


pd.read_sql_query('''
SELECT count(*)
FROM trips
WHERE duration < 30*60;
''', db)


# In[ ]:


df[df['duration']<600].duration.hist()


# In[ ]:


df = pd.read_sql_query('''
SELECT duration
FROM trips
WHERE duration < 600;
''', db)
df.hist(bins=50)


# In[ ]:


df = pd.read_sql_query('''
SELECT duration
FROM trips
WHERE duration > 400 and duration < 500;
''', db)
df.hist(bins=50)


# In[ ]:


pd.read_sql_query('''
SELECT count(*)
FROM trips
WHERE duration = 480.0;
''', db)


# In[ ]:


df = pd.read_sql_query('''
SELECT duration
FROM trips
WHERE duration % 60 != 0 and duration < 1000;
''', db)
df.hist(bins=50)
df = pd.read_sql_query('''
SELECT duration
FROM trips
WHERE duration < 1000;
''', db)
df.hist(bins=50)


# In[ ]:


df = pd.read_sql_query('''
SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips", SUM(duration)/3600 as "Total Ridden Time (Hrs)"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
''', db)
df


# In[ ]:


df = pd.read_sql_query('''
SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips", SUM(duration)/3600 as "Total Ridden Time (Hrs)"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
''', db)
df[:250].plot.bar(x='Bike Number',figsize=(12,5))


# In[ ]:


df[160:260].plot.bar(x='Bike Number',figsize=(12,5))


# In[ ]:


df = pd.read_sql_query('''
SELECT stations.station AS "Station", trips.sub_type , COUNT(*) AS "Count"
FROM trips 
INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY stations.station, trips.sub_type
ORDER BY COUNT(*) DESC;
''', db)


# In[ ]:


df


# In[ ]:


df[df['sub_type']=='Casual'].plot.hist(bins=10)
df[df['sub_type']=='Registered'].plot.hist(bins=10)


# In[ ]:


df2 = df.set_index(['Station','sub_type']).Count


# In[ ]:


df2


# In[ ]:


df2[:50].unstack().plot(kind='barh',figsize=(12,8))


# In[ ]:


df = pd.read_sql_query('''
SELECT start.municipality AS "Municipality", AVG(trips.duration) AS "Duration"
FROM trips 
INNER JOIN stations AS start
ON trips.start_station = start.id
INNER JOIN stations AS end
ON trips.end_station = end.id
WHERE start.municipality = end.municipality
GROUP BY start.municipality
ORDER BY AVG(trips.duration) DESC;
''', db)


# In[ ]:


df


# In[ ]:


df = pd.read_sql_query('''
SELECT *
FROM stations;
''', db)
df

