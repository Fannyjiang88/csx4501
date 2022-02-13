#!/usr/bin/env python
# coding: utf-8

# ## Programming with Python:  Python Basics

# ![image.png](attachment:image.png)

# ## Assignment preliminary note

# This notebook assignment is intended to refresh your Python for the rest of the course.
# 
# * If you're already proficient in the fundamentals, feel free to skip any explanations and simply complete the cells labeled "Exercise"

# ## Python general review

# Python was developed by Guido van Rossum and released in 1991.
# 
# Its core philosophy includes aphorisms like:
# * Beautiful is better than ugly.
# * Explicit is better than implicit.
# * Simple is better than complex.
# * Complex is better than complicated.
# * Readability counts.
# 

# "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
# 
# * Interpreted -- you don't have to compile Python code in order to run it.
# * The simplicity and readability can increase productivity
# * It can be very easy to learn, but it's also a powerful language with many libraries that enhance its ability to efficiently tackle a wide range of computational problems.

# Another interesting tidbit -- "Python" comes from Monty Python's Flying Circus, rather than the snake.

# ## Various ways to run Python code

# * Interactively at a prompt
# * With a file that contains the code you want
# * Inside of an interactive development environment

# ## Calculating

# Simple example: compound interest calculator with annual contributions
# 
# * p = principal
# * r = annual interest rate in percent
# * y = year of the balance
# * c = annual contribution (made at the start of the year)
# 
# $$\text{Balance}(y) = p(1 + r)^y + c\left[\frac{(1 + r)^{y+1} - (1 + r)}{r} \right]$$

# The following two cells assign values to variables and carry out mathematical calculations with the variables to find the balance.

# In[ ]:


y1 = 1
p1 = 1000
r1 = 0.05
c1 = 100
p1*(1 + r1)**y1 + c1*( ((1 + r1)**(y1 + 1) - (1 + r1)) / r1 )


# In[ ]:


y2 = 45
p2 = 1
r2 = 0.05
c2 = 6500
p2*(1 + r2)**y2 + c2*( ((1 + r2)**(y2 + 1) - (1 + r2)) / r2 )


# Note, by the way, that this shows that a 20-yr-old investing \\$1 initially and \\$6500 per year at 5% annual interest will be a millionare by 65.

# ## Strings

# Strings are sequences of characters delimited by either single or double quotes.

# In[ ]:


parrotreturn = "This parrot is no more! It has ceased to be!"


# Strings can be indexed.  Do note that Python indexing starts at 0, not 1.

# In[ ]:


parrotreturn[1]


# In[ ]:


parrotreturn[0]


# Slicing can be used to return subsets.  The first indexed element is included, up to but not including the last indexed character.

# In[ ]:


parrotreturn[0:3]


# In[ ]:


parrotreturn[0:4]


# A Python method can be used to return the element index of a character within the string.

# In[ ]:


parrotreturn.index('!')


# What exactly is ".index"? -- index is a *method* and the "." notifies Python to call the method associated with parrotreturn.

# ---

# ## Exercise

# In[ ]:


# Use parrotreturn.index('!') and slicing to print out only the first sentence of the string


# ---

# Let's check again what parrotreturn holds by explicitly printing it.

# In[ ]:


print(parrotreturn)


# Surrounding the string by single quotes will enable you to include the double quotes as part of the string.

# In[ ]:


parrotreturn = '"This parrot is no more! It has ceased to be!"'


# In[ ]:


print(parrotreturn)


# The same can be achieved within double-quotes by escaping the desired " marks with a backslash.

# In[ ]:


parrotreturn = "\"This parrot is no more! It has ceased to be!\""


# In[ ]:


print(parrotreturn)


# The backslash escape is also useful for escaping other characters, such as newlines (\n)

# In[ ]:


parrotreturn = "\"This parrot is no more!\"\n\"It has ceased to be!\""


# In[ ]:


print(parrotreturn)


# Strings can be concatenated and expanded with math operators.

# In[ ]:


"spam"


# In[ ]:


"spam"*3


# In[ ]:


'spam'*3 + ' and ham and eggs'


# In[ ]:


return3 = "It's expired and gone to meet its maker!"


# In[ ]:


parrotreturn + return3


# In[ ]:


print(parrotreturn + return3)


# ---

# ## Exercises

# In[ ]:


# clean up the quote so that the formatting is consistent


# In[ ]:


# put the entire string into one variable
# and use the bracket syntax with slicing to print only the middle sentence


# ---

# ## Lists

# List are similar in concept to arrays.  They are surrounded by square brackets, and the elements are separated by commas.

# In[ ]:


holyhandgrenade = [1, 2, 5]


# Their indexing is similar to that seen above for strings.

# In[ ]:


holyhandgrenade[1]


# In[ ]:


holyhandgrenade[0]


# In[ ]:


# This will give an error: lists cannot be indexed outside of their range
holyhandgrenade[3]


# But... they can be indexed with negative numbers -- this counts from the end of the array, starting with -1 for the last element.

# In[ ]:


holyhandgrenade[-1]


# In[ ]:


holyhandgrenade[-3]


# In[ ]:


# Indexing too far in the negative direction will also give an error
holyhandgrenade[-4]


# Slices hold for negative indexing.

# In[ ]:


holyhandgrenade[-3:-1]


# In[ ]:


holyhandgrenade[-3:0]


# If you leave one index out (or both), Python assumes you want to go to the beginning and/or end of the array.

# In[ ]:


holyhandgrenade[-3:]


# In[ ]:


holyhandgrenade[:]


# In[ ]:


holyhandgrenade[2]


# List are mutable, so you can reassign the value of individual elements.

# In[ ]:


holyhandgrenade[2] = 3


# In[ ]:


holyhandgrenade[:]


# Lists can also hold other data types such as strings.

# In[ ]:


holyhandgrenade = ['one','two','five']


# In[ ]:


holyhandgrenade


# Lists come with their own set of methods.

# In[ ]:


holyhandgrenade.sort()


# In[ ]:


# sort is alphabetical for strings
holyhandgrenade


# In[ ]:


holyhandgrenade.reverse()


# In[ ]:


# reverse is also alphabetical for strings
holyhandgrenade


# There are several ways to get more information and help about variables and methods.

# In[ ]:


help(holyhandgrenade)


# In[ ]:


holyhandgrenade.append('three')


# In[ ]:


holyhandgrenade


# In[ ]:


print(holyhandgrenade.__doc__)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'holyhandgrenade')


# In[ ]:


type(holyhandgrenade)


# ---

# ## Exercises

# In[ ]:


# make your own list with 5+ elements


# In[ ]:


# try out the "pop" method to see what it does, then try it with a value between the parentheses


# ---

# ## Tuples, sets, and dictionaries

# Python has several ways to denote collections of elements
# * Tuples are surrounded by parentheses; they are immutable
# * Sets are surrounded by curly braces; they are similar to mathematical sets in that they are not ordered (one cannot then refer to elements by an index) but one can test whether an element is in a set or what elements are in the intersection and union of two sets
# * Dictionaries are also surrounded by curly braces, but importantly, they also include explicit "keys" for referring to "values"

# ### Tuples

# In[ ]:


riddleanswers = ('Lancelot', 'Holy Grail', 'blue')


# In[ ]:


riddleanswers[2]


# In[ ]:


# This gives an error because tuples are immutable
riddleanswers[2] = 'green'


# In[ ]:


riddleanswers = ('Lancelot', 43, ['x','y','z'])


# In[ ]:


riddleanswers[2]


# ### Sets

# In[ ]:


riddleanswers = {'Lancelot', 'Holy Grail', 'blue'}


# In[ ]:


# This gives an error because their is no index/order to elements in a set
riddleanswers[2]


# In[ ]:


'blue' in riddleanswers


# In[ ]:


riddleanswers


# In[ ]:


riddleanswers.add('green')


# In[ ]:


riddleanswers


# In[ ]:


riddleanswers.add('blue')


# In[ ]:


riddleanswers


# ### Dictionary

# In[ ]:


riddleanswers = {'name':'Lancelot', 'quest':'Holy Grail', 'favorite colour':'blue'}


# In[ ]:


# This gives an error because dictionaries are indexed by their own set of keys
riddleanswers[2]


# In[ ]:


riddleanswers['favorite colour']


# In[ ]:


riddleanswers.keys()


# In[ ]:


riddleanswers.values()


# ---

# ## Exercises

# In[ ]:


# Add a new key/value pair to riddleanswers


# In[ ]:


# Do a quick search on Google and see if you can figure out how to remove "name":"Lancelot" from the dict


# ---

# ## Conditionals and Loops

# Mathematical conditions:
# * Equals: `==`
# * Does not equal: `!=`
# * Less than: `<`
# * Less than or equal to: `<=`
# * Greater than: `>`
# * Greater than or equal to: `>=`

# In[ ]:


3 == 4


# In[ ]:


3 != 4


# In[ ]:


3 < 4


# In[ ]:


3 <= 4


# In[ ]:


3 > 4


# In[ ]:


3 >= 4


# ### Executing commands based on a condition:  if, elif, and else

# In[ ]:


if 3 == 4:
    print('3 is equal to 4')


# In[ ]:


if 4 == 4:
    print('This is self-evident')


# Python uses indentation to define blocks of code
# * this is not merely a matter of style in Python
# * it is *very* important for defining blocks of code
# * it is up to you how many spaces you want to use for indentation, as long as you are consistent
# * you can not mix tabs and spaces -- here in Jupyter, the indentation is set automatically to 4 spaces

# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 > 4:
    print('3 is greater than 4')


# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 < 4:
    print('3 is less than 4')


# In[ ]:


if 3 == 4:
    print('3 is equal to 4')
elif 3 > 4:
    print('3 is greater than 4')
else:
    print('3 is not equal to or greater than 4')


# Combine conditions:
# * and
# * or
# * not

# In[ ]:


(1==1) and (2==2)


# In[ ]:


(1==2) or (2==2)


# In[ ]:


not(1==2)


# In[ ]:


claim = 5
if claim == 1 or claim == 2:
    print('do not throw the grenade yet')
elif claim == 3:
    print('throw the grenade')
elif claim == 5:
    print('Silly Arthur.  3 comes after 2.')
else:
    print('You are too late - kaboom!')


# ---

# ## Exercise

# In[ ]:


# Switch the value of claim above several times and execute
# Make sure you follow the logic of the resulting print statement.


# ---

# ### While loops

# In[ ]:


## Do not execute something like this!
## It will give you an infinite loop because there is no updating of the loop variable
#disneytrip = 0
#while disneytrip == 0:
#    print('Are we there yet?')


# In[ ]:


# The following will also give an error
disneytrip = 0
while disneytrip < 10:
    print(disneytrip + ': Are we there yet?')
    disneytrip += 1


# It can be very useful to learn how to decipher these error messages.
# 
# Though we don't often pause to reflect on it, "add" depends on context -- Adding 2 + 2 is different than "adding" me to your list of workshop instructors

# In[ ]:


disneytrip = 0
while disneytrip < 10:
    print(str(disneytrip) + ': Are we there yet?')
    disneytrip += 1


# ### For loops

# In[ ]:


for disneytrip in range(10):
    print(str(disneytrip) + ': Are we there yet?')


# In[ ]:


for letter in parrotreturn:
    print(letter)


# You can bypass print's inclusion of the newline by specifying the end character to be nothing.

# In[ ]:


for letter in parrotreturn:
    print(letter, end='')


# "For" is also useful and very intuitive for iterating over dictionaries.

# In[ ]:


riddleanswers


# In[ ]:


for k in riddleanswers:
    print(k)


# In[ ]:


for k in riddleanswers:
    print(riddleanswers[k])


# In[ ]:


for key, value in riddleanswers.items():
    print(key + ': ' + value)


# range(start,end,interval) can be used to iterate over some set of integers.

# In[ ]:


for i in range(3):
    print(i)


# In[ ]:


for i in range(1,4):
    print(i)


# ---

# ## Exercise

# In[ ]:


# Create a for loop that prints the sequence 1, 2, 5


# ---

# ## Functions

# Back to our simple example of a compound interest calculator with annual contributions
# 
# * p = principal
# * r = annual interest rate in percent
# * y = year of the balance
# * c = annual contribution (made at the start of the year)
# 
# $$\text{Balance}(y) = p(1 + r)^y + c\left[\frac{(1 + r)^{y+1} - (1 + r)}{r} \right]$$

# Ideally we'd like to plug in a bunch of numbers and see what comes out.
# 
# Functions allow you to collect together a block of code, name it, and run it when called.
# 
# You can pass data into functions and you can get results returned from functions.

# In[ ]:


## Functions start with "def"
## then the function name, followed immediately by parentheses and parameter list
## and the function body, indented
## The function ends when the indentation stops on a given line

def f():
    print('Hello World!')


# In[ ]:


f()


# In[ ]:


def f2(a):
    return a*2


# In[ ]:


f2


# In[ ]:


f2(3)


# In[ ]:


f2(a=4)


# In[ ]:


def f(p,r,y,c):
    return p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r )


# In[ ]:


year = 1
principal = 1000
rate = 5
annual_contribution = 100
f(principal, rate, year, annual_contribution)


# In[ ]:


year = 1
principal = 1000
rate = 5
annual_contribution = 100
f(principal, rate/100, year, annual_contribution)


# In[ ]:


year = 45
principal = 1000
rate = 5
annual_contribution = 6500
f(principal, rate/100, year, annual_contribution)


# In[ ]:


# The following includes some fancier string formatting
def f2digit(p,r,y,c):
    r = r/100
    return '{:.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))


# In[ ]:


year = 45
principal = 1000
rate = 5
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# In[ ]:


def f2digit(p,r,y,c):
    r = r/100
    amountsaved = '{:.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))
    saying = "If you save for " + str(y) + " years, then you'll have $" + amountsaved + " in your retirement."
    return saying


# In[ ]:


year = 45
principal = 1000
rate = 5
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# What if you want commas in your number?
# 
# * Google is a fantastic reference for python questions
# * Many many common questions have already been asked and answered
# * A quick search may lead you right to the answer you need
# (https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string)

# In[ ]:


def f2digit(p,r,y,c):
    r = r/100
    amountsaved = '{:,.2f}'.format(p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r ))
    saying = "If you save for " + str(y) + " years, then you'll have $" + amountsaved + " in your retirement."
    return saying


# In[ ]:


year = 45
principal = 1000
rate = 5
annual_contribution = 6500
f2digit(principal, rate, year, annual_contribution)


# To follow up on this after class, you may find it interesting to check out the documentation for Python.
# * The answers on that stackoverflow page have a link for PEP (Python Enhancement Proposal) and thereby to https://www.python.org/
# * The page also has another link for the official documentation (https://docs.python.org/3/)
# * You may not immediately appreciate all the points on the documentation site, but that is ok.
# * It's intended to be a complete reference, and therefore reading through it is like reading through a dictionary -- not necessarily fun, but comprehensive
# 

# ---

# ## Exercises

# In[ ]:


# Write your own function definition


# In[ ]:


# Call your function several times to make sure it works


# ---

# ## Modules

# A module is like a library book containing code.  You can write your own module files that include functions you want to save or variables that you want to associate with the code.  
# 
# You can fetch a module using "import", and then all of its variables and functions will be usable inside the local code you are running.  It's therefore very useful for using code that others have already written.

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


# ---
# ## Exercise

# In[ ]:


# Write your own separate module file,
# import the module,
# and execute several cells of code to test its functionality


# In[ ]:





# In[ ]:





# ---

# ## End
