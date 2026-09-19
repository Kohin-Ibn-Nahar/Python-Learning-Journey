'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000. 
Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
'''
q = float(input("Enter Quantity : "))

t = q*100

if t>1000:
    t = t- (t*10/100)

print("Total Cost = ",t)
