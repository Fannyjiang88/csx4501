#!/usr/bin/env python
# coding: utf-8

# # Navigating the notebook

# ### Menu bar
# 
# ![menu bar](images/jupytermenu.png)
# 
# * contains actions for the notebook, its cells, and the kernel

# ### Tool bar
# 
# ![tool bar](images/toolbar.png)
# 
# * buttons for common actions
# * hover over a button for info

# ### Execution Modes
# * **Edit mode**:  changing the content within a cell
#   
#   
# * **Command mode**:  performing actions on the notebook as a whole
# 
# 
# |  _ | Edit | Command |
# | --- | --- | --- |
# | typing | inserts text | executes actions |
# | cursor |   inside cell | none |
# | "Mode" indicator at bottom | "Edit" | "Command" |
# | how to get into it: | `Enter` | `Esc` |
# | _ | (or mouse click/double-click) |

# In[ ]:


# Make this cell go back and forth between edit and command mode


# ### Types of cells
# 
# * **Code** and **Markdown**

# In[ ]:


# This is a code cell


# This is a markdown cell

# ### We will come back to markdown, but first:  Running Code
# 
# First and foremost, the Jupyter Notebook is an interactive environment for writing and running code. The notebook is capable of running code in a wide range of languages. 
# 
# Each notebook is associated with a single kernel.  This notebook is associated with the IPython kernel and therefore runs Python code.

# ### Code cells allow you to enter and run code
# 
# Run a code cell using `Shift-Enter` or pressing the ![run](images/runbutton.png) button in the toolbar above:

# In[ ]:


a = 5


# In[ ]:


print(a)


# There are two other keyboard shortcuts for running code:
# 
# * `Alt-Enter` runs the current cell and inserts a new one below.
# * `Ctrl-Enter` run the current cell and enters command mode.

# ### Markdown cells allow you to enter marked-up text for descriptions, equations, etc.

# (double-click on this cell to see the markdown text)
# 
# *Italic* and **bold** text
# 
# * Bullet lists
# * or numbered lists
#   1. like 1
#   1. or 2
#   1. or 3
# 
# Inline equations like $e^{i\pi} = -1$ or displayed equations like $$e^x = \sum_{i=0}^{\infty} \frac{x^i}{i!}$$
# 
# Or links, like to a [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

# ### Restarting the kernels
# 
# The kernel maintains the state of a notebook's computations. You can reset this state by restarting the kernel. This is done by clicking on the <button class='btn btn-default btn-xs'><i class='fa fa-repeat icon-repeat'></i></button> in the toolbar above.

# ### Run menu
# 
# The "Run" menu has a number of menu items for running code in different ways. These include:
# 
# * Run Selected Cells
# * Run Selected Cells and Insert Below
# * Run Selected Cells and Don't Advance
# * Run Selected Text or Current Line in Console
# * Run All Above Selected Cell
# * ... etc ...

# ### Large outputs
# 
# To better handle large outputs, the output area can be collapsed. Run the following cell and then single-click on the active bar to the left of the output:

# In[ ]:


for i in range(100):
    print(i)


# Beware that output may not scroll automatically:

# In[ ]:


for i in range(500):
    print(2**i - 1)


# ## Useful commands
# 
# * You can save yourself some time by remembering some common commands:
#     * **Basic**
#         * `Enter` -- go into Edit mode
#         * `Shift-Enter` -- execute the active cell
#         * `up-arrow / k` and `down-arrow / j` move the active cell selection
#     * **Saving**
#         * Check the file menu for the short-cut key to save the notebook
#     * **Cell Types**
#         * `y` for code, `m` for markdown
#     * **Cell Creation**
#         * `a` for creating cell above the active one, `b` for below
#     * **Cell Editing**
#         * `x` - cut, `c` - copy, `v` - paste, `d,d` -- "d" pressed twice will delete a cell
#         * `z` - undo deletion
#     * **HELP!!**
#         * `h`
#         * or go to Help Menu -> Keyboard Shortcuts

# # When finished:
# 
# * Be sure to save any changes that you want to keep: File -> Save Notebook
# * Select File -> Close and Shutdown Notebook
# 
# Running notebooks may eat up your available memory! (Shown as "Mem:" on the bottom)

# # Reference:  
# * Help Menu -> User Interface Tour
# * "Running Code.ipynb" taken from https://github.com/jupyter/notebook
# (notebook/docs/source/examples/Notebook/Running Code.ipynb)
# * See also https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html
