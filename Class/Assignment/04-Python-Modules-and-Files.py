#!/usr/bin/env python
# coding: utf-8

# # Using modules to work with files

# ## Modules

# A lot of coders have written Python code that you can easily reuse.  
# 
# Some code comes standard with every Python installation.  Other code needs to be retrieved and installed.  However, once you have the code, it can dramatically expand your coding capabilities.
# 
# Modules allow us to use externally developed code.
# * A module is a group of code items such as functions that are related to one another. Individual modules are often grouped together as a library.
# * Modules can be loaded using `import <modulename>`. Functions that are part of the module `modulename` can then be used by typing `modulename.functionname()`. 
#   * For example, `sin()` is a function that is part of the `math` module
#   * We can use to by typing `math.sin()` with some number between the parentheses.
# * Modules may also contain constants in addition to functions.
#   * The `math` module includes a constant for $\pi$ -- `math.pi`

# In[ ]:


import math


# In[ ]:


math.pi


# In[ ]:


math.sin(math.pi/2)


# We can even write our own modules!
# 
# Open the included "mymodule.py" file and look it over before executing the following cells.

# In[ ]:


import mymodule


# In[ ]:


dir(mymodule)


# In[ ]:


mymodule.holyhandgrenade


# In[ ]:


for i in range(len(mymodule.holyhandgrenade)):
    print(mymodule.holyhandgrenade[i])


# One can import select functions or variables from a module, as well as rename them with an alias.

# In[ ]:


from mymodule import holyhandgrenade as hhg


# In[ ]:


hhg


# In[ ]:


import mymodule as mm


# In[ ]:


mm.holyhandgrenade


# The help documentation from the module's function is the initial part of the function body delimited by triple-quotes.

# In[ ]:


help(mymodule.compound_calculator)


# In[ ]:


print(mymodule.compound_calculator.__doc__)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'mymodule.compound_calculator')


# In[ ]:


mymodule.compound_calculator(1000,5,1,100)


# In[ ]:


mm.riddleanswers


# In[ ]:


mm.stocksDict


# <div class="alert alert-info">
# 
# <b>When you review this notebook later, try writing your own separate module file, importing the module, and executing several cells of code to test its functionality</b>
# 
# </div>

# ## Working with files

# Here we're going to be working with the Classics dataset obtained off the [CORGIS website](https://corgis-edu.github.io/corgis/) (The Collection of Really Great, Interesting, Situated Datasets)
# 
# I have already taken the liberty of sharing the files with you.
#   * `classics.csv` is a comma-separated value file containing the data
#   * `classics.json` is a JSON file containing the data
#   * `classics.data` and `classics.py` are files that you can use more directly with Python
#     * `classics.py` is a module file

# In[ ]:


import classics


# In[ ]:


book = classics.get_book()


# We don't know what `book` is yet, so let's find out

# In[ ]:


type(book)


# And let's get some more info

# In[ ]:


len(book)


# In[ ]:


book[0]


# That's kinda hard to chew off, so let's pretty print it

# In[ ]:


from pprint import pprint as prettyprint


# In[ ]:


prettyprint(book[0])


# In[ ]:


book[0].keys()


# In[ ]:


for i in book:
    print(str(i['metadata']['downloads']) + ': ' + i['bibliography']['title'])


# ## We actually know enough Python now that we could use other libraries to work with the CSV and JSON files

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv('classics.csv')


# In[ ]:


df


# In[ ]:


df.hist('metadata.downloads',bins=100)


# In[ ]:


df = pd.read_json('classics.json')


# In[ ]:


df


# # We'll look more into this next week!!
