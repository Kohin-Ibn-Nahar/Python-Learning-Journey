"""
Write a program to prompt the user for hours and rate per hour to compute gross pay. 
However, the employee who worked above 40 hours give them 1.5 times the hourly rate 
for individual hours.
          Enter Hours: 45
          Enter Rate: 10
          Pay: 475.0
"""
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = 0

if hours > 40:
    pay = (40 * rate) + ((hours - 40)*rate*1.5)

else :
    pay = hours*rate

print("Pay: ",pay)
