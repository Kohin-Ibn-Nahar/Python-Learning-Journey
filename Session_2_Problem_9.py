'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended. Is student is allowed to sit in exam or not.
'''
h = int(input("Number of Classes Held: "))
a = int(input("Number of Classes Attended: "))

p = a/h * 100
print("Percentage of Class Attended : ",p)

if p<75:
    print("Not Allowed")
else:
    print("Allowed")
