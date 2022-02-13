#!/usr/bin/env python
# coding: utf-8

# # Geopandas and census data
# This notebook was originally authored by Yoh Kawano, spatial data scientist extraordinaire in UCLA's Office for Advanced Research Computing. 
# 
# If you get into coding, a lot of your work will be trying to learn code and details about code libraries on your own!  I would like you to go through all of the subsequent cells, read them, absorb what the results of the code execution are, and look up any pieces of code that do not make sense.  When you finally make it through, you will be producing plots of spatial census data.
# 
# This notebook includes:
# 
# - how and where to find and download census data
# - use `geopandas` library to read a geojson file
# - use `contextily` to add basemaps ([documentation](https://contextily.readthedocs.io/en/latest/intro_guide.html))
# - renaming columns
# - normalizing data columns
# - simple stats
# - adding basemaps

# ## Where to get census data?
# 
# 
# Well, you have many options, including getting it directly from the source, the [census bureau website](https://www.census.gov/data.html) itself. We also have, as part of the academic community, a great resource: [Social Explorer](https://www.socialexplorer.com/). With a campus-wide license to have full access to their website, you can download any census variable, that pretty much existed... ever. And, with its easy-to-use user interface, this is a wonderful one-stop shop for your census needs.
# 
# But for data scientists, I recommend another source: [censusreporter.org](https://censusreporter.org/)
# 
# <a href="https://censusreporter.org" target="_blank"><img src="images/cr.png"></a>

# # Data
# 
# For the purposes of this assignment, the data is already made available inside the file `data/acs2019_5yr_B03002_14000US06037222001.geojson`

# ## The libraries
# 
# Note: it will be okay to get a warning.

# In[ ]:


# for general data wrangling tasks
import pandas as pd

# to read and visualize spatial data
import geopandas as gpd

# to provide basemaps 
import contextily as ctx

# to give more power to your figures (plots)
import matplotlib.pyplot as plt


# ## Importing data
# 
# In order to work with data in python, we need a library that will let us handle "spatial data exploration." For this notebook, we will use geopandas to read and wrangle a [geojson](https://en.wikipedia.org/wiki/GeoJSON) file.
# 
# Before continuing, try taking a little detour to find out how geojson files are constructed:
# 
# - [geojson.io](http://geojson.io/#map=2/20.0/0.0)
# 
# ![geojson](images/geojson.png)

# We make the call to load and read the data that was downloaded from census reporter. Take note of the relative path reference to find the file in your file directory.

# In[ ]:


# load a data file
# note the relative filepath! check where this file is located in your file list at left
gdf = gpd.read_file('data/acs2019_5yr_B03002_14000US06037222001.geojson')


# ## Preliminary inspection
# A quick look at the size of the data.

# In[ ]:


gdf.shape


# In[ ]:


gdf.head()


# In[ ]:


# plot it!
gdf.plot(figsize=(10,10))


# In[ ]:


gdf.sample()


# ## Data types
# 
# To get the data types, we will use `.info()`. 

# In[ ]:


# look at the data types
gdf.info()


# ### The FIPS code
# What is the geoid? It is called a FIPS code but why is it important?
# 
# - https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html
# 
# ![fips](images/fips.png)

# In[ ]:


gdf.geoid.head()


# ![fips code](https://learn.arcgis.com/en/related-concepts/GUID-D7AA4FD1-E7FE-49D7-9D11-07915C9ACC68-web.png)
# 
# [Source: ESRI](https://learn.arcgis.com/en/related-concepts/united-states-census-geography.htm)

# ## Delete county row
# 
# As we have observed, the first row in the data obtained from censusreporter is for the entire county. Keeping this row is problematic, as it represents a data record that is at a different scale. Let's delete it.

# <div class="alert alert-danger">
#     <b>Important!</b><hr>
#     Note that any data downloaded from censusreporter will have a "summary row" for the entire data.
# </div>

# In[ ]:


# check the data again
gdf.head()


# In[ ]:


# drop the row with index 0 (i.e. the first row)
gdf = gdf.drop([0])


# In[ ]:


# check to see if it has been deleted
gdf.head()


# ## The census data dictionary
# There are a lot of columns. What are these columns? Column headers are defined in the `metadata.json` file that comes in the dowloaded zipfile from censusreporter. Click the link below to open the json file in another tab.
# 
# * [metadata.json](data/metadata.json)

# For the purposes of this exercise, we will not choose to analyze subcategories within the Hispanic category, nor will we analyze breakdowns within the multiple race category.  Let's identify which columns are needed, and which are not for our exploration.  
# 
# 
# ![census variables](images/census1.png)

# ## Dropping columns 
# There are many columns that we do not need. 
# 
# - output existing columns as a list
# - create a list of columns to keep
# - redefine `gdf` with only the columns to keep
# 

# In[ ]:


list(gdf) # this is the same as df.columns.to_list()


# In[ ]:


# columns to keep
columns_to_keep = ['geoid',
 'name',
 'B03002001',
 'B03002002',
 'B03002003',
 'B03002004',
 'B03002005',
 'B03002006',
 'B03002007',
 'B03002008',
 'B03002009',
 'B03002012',
 'geometry']


# In[ ]:


# redefine gdf with only columns to keep
gdf = gdf[columns_to_keep]


# In[ ]:


# check the slimmed down gdf
gdf.head()


# ## Renaming columns
# 
# Let's rename the columns. First, create a list of column names as they are now.

# In[ ]:


list(gdf) # this is the same as df.columns.to_list()


# Then, simply copy and paste the output list above, and define the columns with it. Replace the values with your desired column names

# In[ ]:


gdf.columns = ['geoid',
 'name',
 'Total',
 'Non Hispanic',
 'Non Hispanic White',
 'Non Hispanic Black',
 'Non Hispanic American Indian and Alaska Native',
 'Non Hispanic Asian',
 'Non Hispanic Native Hawaiian and Other Pacific Islander',
 'Non Hispanic Some other race',
 'Non Hispanic Two or more races',
 'Hispanic',
 'geometry']


# In[ ]:


gdf.head()


# ## Double check your data integrity
# Does the math add up? Let's check. The `Total` should equal the rest of the columns.

# In[ ]:


# get a random record
random_tract = gdf.sample()
random_tract


# To get values from individual cells in a dataframe, use the `iloc` command.
# 
# - `iloc` ([documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html))
# 
# While there are various methods to get cell values in python, the iloc command allows you to get to a cell based on the position of the record row and the column name.

# In[ ]:


# example usage of iloc to get the total population of our random record
# "for the 0th record, get the value in the Total column"
random_tract.iloc[0]['Total']


# In[ ]:


# print this out in plain english
print('Total population: ' + str(random_tract.iloc[0]['Total']))


# In[ ]:


# non hispanic plus hispanic should equal to the total
print('Non Hispanic + Hispanic: ' + str(random_tract.iloc[0]['Non Hispanic'] + random_tract.iloc[0]['Hispanic']))


# In[ ]:


# hispanic plus all the non hispanice categories
print(random_tract.iloc[0]['Non Hispanic White'] + 
      random_tract.iloc[0]['Non Hispanic Black'] + 
      random_tract.iloc[0]['Non Hispanic American Indian and Alaska Native'] + 
      random_tract.iloc[0]['Non Hispanic Asian'] + 
      random_tract.iloc[0]['Non Hispanic Native Hawaiian and Other Pacific Islander'] + 
      random_tract.iloc[0]['Non Hispanic Some other race'] + 
      random_tract.iloc[0]['Non Hispanic Two or more races'] + 
      random_tract.iloc[0]['Hispanic'])


# ## Simple stats and plots

# In[ ]:


# access a single column like df['col_name']
gdf['Total'].head()


# In[ ]:


# What is the mean?
gdf['Total'].mean()


# In[ ]:


# What is the median?
gdf['Total'].median()


# In[ ]:


# get some stats
gdf['Total'].describe()


# In[ ]:


# plot it as a historgram with 50 bins
gdf['Total'].plot.hist(bins=50)


# <div class="alert alert-info">
#     Now it's your turn. Find some stats for different fields in the data and output them below.
#     </div>

# In[ ]:





# ## Sorting
# What are the top 10 most populated census tracts? What are the census tracts with the highest black popluation? To answer these questions, the simplest method is to sort the data by their respective columns.

# In[ ]:


gdf_sorted = gdf.sort_values(by='Total',ascending = False)


# In[ ]:


# display the data, but just a few columns to keep it clean
gdf_sorted[['geoid','Total']].head(10)


# In[ ]:


# plot it
gdf_sorted.head(10).plot()


# In[ ]:


# Make it prettier
gdf_sorted.head(100).plot(figsize=(10,10),column='Total',legend=True)


# <div class="alert alert-info">
#     Now it's your turn! Create a table and accompanying bar plot for the top/bottom x values for column of your choice.
#     
#     
# When you are done, post your map to the <a href="https://docs.google.com/document/d/1FjLOg2SBYaUn-k5mzk_WL5SgcL7neLg3vkmSRC_37-8/edit?usp=sharing" target="_blank">class gallery</a> (right click the image, copy, and paste)
# 
# </div>

# In[ ]:





# ## Filtering and subsetting data
# Sorting is one method, but the process of discovery compels us to interrogate the data in different ways. One method of doing so is to query, or filter the data to see specific views of the data based on a question you may have. For example, what are the census tracts that have no people in them? Or, Which census tracts are more than 75% black?

# In[ ]:


# subset the data so that we can see the data per row... 
# in other words, this syntax is asking to "show me the values in my dataframe that match this filter
gdf[gdf['Total']==0]


# Note that unless you specify the resulting output as a new variable, the results are only temporary (in memory). If you want to use the results for subsequent analysis, you need to create a new variable.

# In[ ]:


# create a new variable for census tracts with zero pop
gdf_no_pop = gdf[gdf['Total']==0]


# In[ ]:


# how many records?
print('There are ' + str(len(gdf_no_pop)) + ' census tracts with no people in them')


# In[ ]:


# display it
gdf_no_pop[['geoid','Total']]


# ## Totals are great but let's normalize the data
# 
# For almost any data inquiry, you should ask the question: should I normalize the data? With raw numbers, is it fair to compare one census tract to another? For example, if one census tract has 1000 hispanics, and another has 100, can we assume that the first tract is largely Hispanic? No, because the total population might be 10000 people, resulting in it being 10% hispanic, whereas the second tract might have 200 people living in it, resulting in it being 50% hispanic.

# To avoid these types of misrepresentations, we can normalize the data, and provide it as a percent of total.

# In[ ]:


# output columns
list(gdf)


# In[ ]:


# create a new column, and populate it with normalized data to get the percent of total value
gdf['Percent Non Hispanic'] = gdf['Non Hispanic']/gdf['Total']*100
gdf['Percent Hispanic'] = gdf['Hispanic']/gdf['Total']*100


# In[ ]:


gdf.sample(5)


# <div class="alert alert-info">
# Now it's your turn!
# 
# Create new columns for 
# - `Percent Non Hispanic White`
# - `Percent Non Hispanic Black`
# - `Percent Non Hispanic American Indian and Alaska Native`
# - `Percent Non Hispanic Asian`
# - `Percent Non Hispanic Native Hawaiian and Other Pacific Islander`
# - `Percent Non Hispanic Some other race`
# - `Percent Non Hispanic Two or more races`
#     </div>

# In[ ]:





# # Maps!

# We can now create choropleth maps in geopandas. 
# 
# * [geopandas choropleth maps](https://geopandas.org/mapping.html#choropleth-maps)
# * [color schemes with mapclassify](https://pysal.org/notebooks/viz/mapclassify/intro.html)
#   * `natural_breaks`
#   * `equal_interval`
#   * `quantiles`
#   * etc...

# In[ ]:


# The value passed into the `column` parameter specifies which column's values are plotted
gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='NaturalBreaks')


# In[ ]:


# Note the different scheme to make for equal breaks in the color legend.
gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='equal_interval')


# In[ ]:


# And you can also plot different quartiles of the data
gdf.plot(figsize=(12,10),
                 column='Percent Hispanic',
                 legend=True, 
                 scheme='quantiles')


# ## Using subplots to create multiple plots
# 
# It is often useful to generate multiple plots next to each other. To do so, we look at matplotlib's `subplot` command:
# 
# - https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html

# In[ ]:


# create the 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(15, 12))

# name each subplot
ax1, ax2 = axs

# regular count map on the left
gdf.plot(column='Percent Hispanic', 
            cmap='RdYlGn_r', 
            scheme='quantiles',
            k=5, 
            edgecolor='white', 
            linewidth=0., 
            alpha=0.75, 
            ax=ax1, # this assigns the map to the subplot,
            legend=True
           )

ax1.axis("off")
ax1.set_title("Percent Hispanic")

# spatial lag map on the right
gdf.plot(column='Percent Non Hispanic Black', 
            cmap='RdYlGn_r', 
            scheme='quantiles',
            k=5, 
            edgecolor='white', 
            linewidth=0., 
            alpha=0.75, 
            ax=ax2, # this assigns the map to the subplot
            legend=True
           )

ax2.axis("off")
ax2.set_title("Percent Non Hispanic Black")


# <div class="alert alert-info">
# 
# Now it's your turn! Create map plots based on other race indicators. Experiment with the different schemes to display variations of the same data, mapped differently.
#     
# When you are done, post your map to the <a href="https://docs.google.com/document/d/1FjLOg2SBYaUn-k5mzk_WL5SgcL7neLg3vkmSRC_37-8/edit?usp=sharing" target="_blank">class gallery</a> (right click the image, copy, and paste)
# 
# </div>

# In[ ]:





# ## Additional mapping ideas
# What does the majority ethnic cluster look like in Los Angeles?

# In[ ]:


gdf[gdf['Percent Hispanic'] > 80]


# In[ ]:


gdf[gdf['Percent Hispanic'] > 90].plot(figsize=(12,10))


# <div class="alert alert-info">
# 
# Now it's your turn! Create map plots based on other race indicators with varying segments of the population.
# 
# When you are done, post your map to the <a href="https://docs.google.com/document/d/1FjLOg2SBYaUn-k5mzk_WL5SgcL7neLg3vkmSRC_37-8/edit?usp=sharing" target="_blank">class gallery</a> (right click the image, copy, and paste)
# 
# </div>

# In[ ]:





# ## Add a basemap
# 
# Adding a basemap to a geopandas plot can be done using the [contextily library](https://contextily.readthedocs.io/en/latest/intro_guide.html). To do so, you must:
# 
# * reproject your geodataframe to Web Mercator (epsg: 3857)
# * add a basemap, use the following [guidelines](https://github.com/geopandas/contextily/blob/master/notebooks/providers_deepdive.ipynb)

# In[ ]:


# reproject to Web Mercator
gdf_web_mercator = gdf.to_crs(epsg=3857)


# In[ ]:


# use subplots that make it easier to create multiple layered maps
fig, ax = plt.subplots(figsize=(15, 15))

# add the layer with ax=ax in the argument 
gdf_web_mercator[gdf_web_mercator['Percent Hispanic'] > 50].plot(ax=ax, alpha=0.8)

# turn the axis off
ax.axis('off')

# set a title
ax.set_title('Census Tracts with more than 50% Hispanic Population',fontsize=16)

# add a basemap
ctx.add_basemap(ax)


# <div class="alert alert-info">
# 
# Now it's your turn! 
# 
# Add your final maps to the <a href="https://docs.google.com/document/d/1FjLOg2SBYaUn-k5mzk_WL5SgcL7neLg3vkmSRC_37-8/edit?usp=sharing" target="_blank">class gallery</a> (right click the image, copy, and paste)
# 
# </div>

# In[ ]:




