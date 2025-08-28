# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 15:03:26 2025

@author: jgoldberg
"""

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist = symbols.split(',')

symlist[0]

symlist[2] = 'AIG'
symlist

symlist[0:3]
symlist[-2]

mysyms = []
mysyms.append('GOOG')
mysyms
symlist[-2:] = mysyms # I forgot the colon and it appended a list instead
symlist

for s in symlist:
    print('s =', s)
    
# membership tests
'AIG' in symlist
'AA' in symlist
'CAT' not in symlist

symlist.append('RHT')
symlist.insert(1, 'AA')
symlist

symlist.remove('MSFT')
symlist

# add a duplicate entry
symlist.append('YHOO')
symlist

symlist[4]

symlist.count('YHOO')

# remove the first occurrence
symlist.remove('YHOO')
symlist

# sorting. Happens in-place
symlist.sort(reverse=True)

# join a list into a string
a = ','.join(symlist)
b = ':'.join(symlist)
c = ''.join(symlist)

nums = [101, 102, 103]
items = ['spam', symlist, nums]

items[0]
items[0][0]
items[1]
items[1][1]
items[1][1][2]
items[2]
items[2][1]


