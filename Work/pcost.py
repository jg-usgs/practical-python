# pcost.py
#
# Exercise 1.27

import os
os.getcwd()
os.chdir(r'C:\Users\jgoldberg\GitHub\practical-python\Work\Data')
os.listdir()

# with open('portfolio.csv', 'rt') as f:
#     data = f.read()
    
# print(data)

# # %%

# for line in data:
#     print(line)
# %%


f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
headers

total = 0

for line in f:
    row =line.split(',')
 
    
    subtotal = int(row[1]) * float(row[2])
    # print('subtotal', subtotal)
    total += subtotal
    # print('total', total)
print('Total cost', total)
f.close()




