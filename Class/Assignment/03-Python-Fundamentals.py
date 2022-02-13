#!/usr/bin/env python
# coding: utf-8

# # Python Fundamentals

# We'll start simple (and get more comfortable with Jupyter notebooks too).
# 
# Execute the below cell by selecting it and typing Shift+Enter on your keyboard.

# In[ ]:


print('Hello world!')


# Welcome to your first python function, `print()`. 
# 
# You are passing an argument to the print function (here the string `'Hello world!'`) -- Python then interprets the command and executes the function with the string as its argument.

# In[ ]:


# Try executing this cell too
print('Hello world!')


# ### Comments
# 
# Any line of Python code that is prefixed with a `#` is considered a comment.  
# * It will not get executed when the code runs
# * It is useful for documenting what the code is doing
#   * For yourself and for others
#   
# All experienced coders agree that code must be well-documented.  It's great if your code achieves fantastic things, but what happens if you come back to it after a month and can't make any sense out of what you wrote?  This is surprisingly easy to do -- you may not rememeber the logic, the caveats, the hours spent trying to figure out how to calculate something.  
# 
# Document your code!

# In[ ]:


# this is a comment. the python interpreter ignores it.
# comments are just notes for humans to read to help understand the code
# best practice: add a comment for every couple lines of code to explain what's going on and why
# you'd be amazed at how quickly you forget your code's logic (at least i always do)


# ## Simple math
# 
# Computers make for great calculators

# | Operation | Symbol            | Example    | Returned Value |
# | -------------- | -------------------- | ---------- | ---------- |
# | addition          | `+` | `3 + 2` | `5`        |
# | subtraction        | `-`       | `3 - 2` | `1`   |
# | multiplication          | `*`    | `3 * 2` | `6`    |
# | division         | `/`   | `3 / 2` | `1.5`    |
# | exponentation         | `**`    | `3 ** 2` | `9`     |
# 

# In[ ]:


# add two integers
2 + 3


# In[ ]:


# multiply the integers
2 * 3


# In[ ]:


# divide two integers to get a floating point number
2 / 3


# In[ ]:


# multiplication gets evaluated before addition
2 + 3 * 4


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# * Try out some math of your own in the next cell.
# * Try adding parentheses to `2 + 3 * 4` to make the addition be evaluated first 
#     
# </div>

# In[ ]:


# Enter code here and execute the cell:


# ### Variables
# 
# **Variables** can be used to store values calculated in expressions and used for other calculations. 
# 
# Assigning values to variables is straightforward. Simply type `variable_name = value`, where `variable_name` is the name of the variable you wish to define.

# In[ ]:


# variables, such as x here, contain values and their values can vary
x = 5


# In[ ]:


# what is the value of x?
x


# In[ ]:


# you can perform operations on variables, just like you can on two numbers
x + 3


# In[ ]:


# what is the value of x now?
x


# In[ ]:


# to update the value of a variable, you need to do an assignment again
x = x + 3


# In[ ]:


# and now what is the value of x?
x


# In[ ]:


# create a new variable y from an operation on x
x = 5
y = x * 2
y


# In[ ]:


# outputting values only displays the last thing output
# this is different from printing! it is kinda confusing!
x
y


# In[ ]:


# use print to write some value(s) to the "console"
print(x)
print(y)


# In[ ]:


# you can comma-separate values to print multiple values to the console on one line
# note that this syntax automatically adds a space between variables
print(x, y)


# In[ ]:


# you can also print the result of an expression
print(x * y)


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# In a single line, create a new variable `z` and set it equal to `x` divided the sum of `x` plus `y`
#     
# </div>

# In[ ]:


# Enter code here and execute the cell:


# ## Strings

# Strings are ordered sequences of characters delimited by either single or double quotes.

# In[ ]:


parrotreturn = "This parrot is no more! It has ceased to be!"


# Nothing was returned above because you only set the value of the `parrotreturn` variable
# 
# The following will return the string and cause it to be output.

# In[ ]:


parrotreturn


# In[ ]:


# You can also explicitly print the string with:
print(parrotreturn)


# In Python, you can get the nth element from an ordered object (like a string) with [n] indexing notation
# * Key note: Python starts the index with zero, not one

# In[ ]:


parrotreturn[1]


# In[ ]:


parrotreturn[0]


# To get more than one character, you can use *slicing*.  Slicing is a way to return subsets and is indicated by `[first, last]`, where `first` is the starting index and `last` is the ending index.
# 
# * Key note: the element at the ending indexed place will not be included.

# In[ ]:


parrotreturn[0:3]


# In[ ]:


parrotreturn[0:4]


# A Python method can be used to return the indexed location of a character within the string.

# In[ ]:


parrotreturn.index('!')


# Recall that Python objects can have their own functions.
# 
# What exactly is ".index"? -- index is a *method* and the "." notifies Python to call the method associated with parrotreturn.

# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# Use `parrotreturn.index('!')` and slicing to print out only the first sentence of the string
#     
# </div>

# In[ ]:


# Enter code here and execute the cell:


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


# In[ ]:


holyhandgrenade.append('three')


# In[ ]:


holyhandgrenade


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# 1. Make your own list with 5+ elements
# 2. Try out the "pop" method to see what it does, then try it with a value between the parentheses
# 
# </div>

# In[ ]:


# Enter your code for #1 here:


# In[ ]:


# Enter your code for #2 here:


# <div class="alert alert-danger">
# 
# <b>Help!!</b>
# 
# </div>

# Sometimes you may need some help in understanding what a variable really is, what functions are available for it, or accessing some kind of help documentation for it.
# 
# The following can be useful:
# * `type`: tells you the data type of the variable
# * `dir`: shows you a list of the attributes and functions that are a part of the object
# * `help`: shows help documentation for a function, provided the code author has written something for it

# In[ ]:


type(holyhandgrenade)


# In[ ]:


dir(holyhandgrenade)


# In[ ]:


help(holyhandgrenade)


# In[ ]:


help(holyhandgrenade.append)


# In[ ]:


print(holyhandgrenade.__doc__)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'holyhandgrenade')


# ## Dictionaries

# Python has several ways to denote collections of elements besides lists.
# 
# Here we will look at dictionaries.  Dictionaries are surrounded by curly braces, but importantly, they include explicit "keys" for referring to "values", as opposed to indexing by numerical order like lists.

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


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# 1. Add a new key/value pair to riddleanswers
# 2. Do a quick search on Google and see if you can figure out how to remove `"name":"Lancelot"` from this dictionary
# 
# </div>

# In[ ]:


# Enter your code for #1 here:


# In[ ]:


# Enter your code for #2 here:


# ## Conditionals and Loops

# Mathematical conditions:
# * Equals: `==`
# * Does not equal: `!=`
# * Less than: `<`
# * Less than or equal to: `<=`
# * Greater than: `>`
# * Greater than or equal to: `>=`

# These are rather straight-forward -- try executing the following cells to check the True and False values.

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


# ### Executing commands based on a condition
# 
# `if`, `elif`, and `else` allow you to execute Python commands only if some condition is satisfied.

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


# You can evaluate more than one True/False condition in the statements by combining conditions with `and`, `or`, and `not`

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


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# Try assigning different values to `claim` below and re-executing the cell several times to make sure you can follow the logic of the resulting print statement.
# 
# </div>

# In[ ]:


# Switch the value of claim to check the logic

claim = 5
if claim == 1 or claim == 2:
    print('do not throw the grenade yet')
elif claim == 3:
    print('throw the grenade')
elif claim == 5:
    print('Silly Arthur.  3 comes after 2.')
else:
    print('You are too late - kaboom!')


# ### For loops
# 
# It can be useful to repeat an operation several times.  *For* loops can be used to repeat a command:
# * a given number of times
#   * special function `range`
#     * `range(n)` returns a sequence of numbers from 0 to n (n not included)
#     * `range(n,m)` returns a sequence of numbers from n to m (m not included)
#     * `range(n,m,i)` returns a sequence of numbers from n to m (m not included) with an interval of i between numbers
# * for every element in a list
# * for every key or value in a dictionary
# * for some iterable set of values

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


# `range` can be useful for iterating over some set of integers.

# In[ ]:


for i in range(3):
    print(i)


# In[ ]:


for i in range(1,4):
    print(i)


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# Create a for loop that prints the sequence 1, 2, 5
# 
# </div>

# In[ ]:


# Enter code here and execute the cell:


# ## Functions

# Let's consider a mathematical operation that we wouldn't want to keep typing every time when run it.
# 
# The following is an equation for calculating compound interest with annual contributions
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


## Functions start with "def",
## then the function name, followed immediately by parentheses, the parameter list,
## and the function body indented.
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


# you can include math operations inside the argument list for the function call
year = 1
principal = 1000
rate = 5
annual_contribution = 100
f(principal, rate/100, year, annual_contribution)


# In[ ]:


# The following shows a function with a two-line body
# The 2nd line includes some fancier string formatting
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


# As you might imagine, functions can extend for an arbitrary number of lines
# and once you get started, functions can be much longer than this
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


# <div class="alert alert-danger">
# 
# What's happening here with the string formatting??  Is there documentation?!
#     
# .... and can I put commas in the number?
#     
# </div>

# * Google is a fantastic reference for python questions
# * Many many common questions have already been asked and answered
# * A quick search may lead you right to the answer you need
# (https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string)

# To follow up on this after class, you may find it interesting to check out the documentation for Python.
# * The answers on that stackoverflow page have a link for PEP (Python Enhancement Proposal) and thereby to https://www.python.org/
# * The page also has another link for the official documentation (https://docs.python.org/3/)
# * You may not immediately appreciate all the points on the documentation site, but that is ok.
# * It's intended to be a complete reference, and therefore reading through it is like reading through a dictionary -- not necessarily fun, but comprehensive
# 

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


# <div class="alert alert-info">
# 
# <b>Your turn:</b>
# 
# 1. Write your own function definition
# 2. Call your function several times to make sure it works
#     
# </div>

# In[ ]:


# Enter your code for #1 here:


# In[ ]:


# Enter your code for #2 here:


# <div class="alert alert-info">
# 
# <b>When you're finished, go into the Canvas site and try this week's Quiz</b>
#     
# </div>
