# mortgage.py
#
# Exercise 1.7

'''
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with 
Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.

Here is a program that calculates the total amount that Dave will have to pay 
over the life of the mortgage:
'''

# this is working

# principal = 500000.0
# rate = 0.05
# payment = 2684.11
# total_paid = 0.0
# months = 0

# for i in range(12):
#     payment = 3684.11
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment   
#     months += 1


# while principal > 0:     
#     payment = 2684.11
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment
#     months += 1

# print('Total paid', total_paid)



principal = 500000.0
# principal = 100000.0
rate = 0.05
payment = 2684.11
# payment = 7000
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
# extra_payment = 1000

while principal > 0:     
# while principal > payment:     
    payment = 2684.11
    # payment = 10000
    extra_payment = 1000
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = payment + extra_payment
    else: payment = payment
    
    principal = principal * (1+rate/12) - payment

    total_paid = total_paid + payment
    months += 1
    print(months, total_paid, principal)
    
    
    

# payment = principal * (1+rate/12)
# # principal = payment
# principal = principal - payment

# total_paid = total_paid + payment
# months += 1
# print(months, total_paid, principal)

# print('Total paid', total_paid)

# adding this line to check freefilesync backup
