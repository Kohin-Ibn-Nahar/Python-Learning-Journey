'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. 
Ask user for their salary and year of service and print the net bonus amount.
'''

salary = float(input("Enter Salary : "))
year = float(input("Enter Year of Service : "))
bonus = 0

if year > 5:
    bonus = salary * 5/100

print("Bonus = ",bonus)
print("Total Salary = ",salary+bonus)
