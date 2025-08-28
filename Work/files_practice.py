# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:41:52 2025

@author: jgoldberg
"""

# open a file
f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)

# read all of the data
data = f.read()

# Read only up to 'maxbytes' bytes
maxbytes = 128
data = f.read([maxbytes])

# write some text
g.write('some text')

# close when you are done
f.close()
g.close()

# Files should be properly closed and it's an easy step to forget. 
# Thus, the preferred approach is to use the with statement like this.

filename = 'foo.txt'
with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
# ...statements

# This automatically closes the file when control leaves the indented code block.

# %% read an entire file all at once as a string

with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`

# %% read a file line-by-line by iterating

with open(filename, 'rt') as file:
    for line in file:
        pass
        # Process the line
# %% write string data

with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
# redirect the print function
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...

# %% okay onto the actual exercises

import os
os.getcwd()
os.chdir(r'C:\Users\jgoldberg\GitHub\practical-python\Work\Data')
os.listdir()

with open('portfolio.csv', 'rt') as f:
    data = f.read()
    
data 
# above gives raw string representation including quotes and escape codes
print(data)
# this is formatted nicely

# %% use next to skip a header row

f = open('portfolio.csv', 'rt')
headers = next(f)
headers
'name,shares,price\n'
for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
f.close()

# %%

f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
headers

for line in f:
    row =line.split(',')
    print(row[1])
f.close()

# %%

# =============================================================================
# Now that you know how to read a file, let’s write a program to perform a simple 
# calculation.
# The columns in portfolio.csv correspond to the stock name, number of shares, and 
# purchase price of a single stock holding. Write a program called pcost.py that 
# opens this file, reads all lines, and calculates how much it cost to purchase 
# all of the shares in the portfolio.
# Hint: to convert a string to an integer, use int(s). To convert a string to a 
# floating point, use float(s).
# 
# Your program should print output such as the following:
# 
# Total cost 44671.15
# =============================================================================

import gzip
with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')