'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended. Is student is allowed to sit in exam or not.

Modify the above question to allow student to sit if he/she has medical cause. 
Ask user if he/she has medical cause or not ('Y' or 'N') and print accordingly.

'''
h = int(input("Number of Classes Held: "))
a = int(input("Number of Classes Attended: "))

p = a/h * 100
print("Percentage of Class Attended : ",p)

temp=""

if p<75:
    temp = "Not Allowed"
else:
    temp = "Allowed"


if temp=="Not Allowed":
    m = input("Do you have any medical cause?(Plz tell only Y/N)")
    if m=='Y' or m=='y':
        temp = "Allowed"

print(temp)
