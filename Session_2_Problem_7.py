'''
A school has following rules for grading system:

a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

'''

score = float(input("Enter score: "))

if score>100 or score < 0:
    print("Invalid Score")
    
else:
    if score >= 80:
        print("A")
    elif score >= 60:
        print("B")
    elif score >= 50:
        print("C")
    elif score >= 45:
        print("D")
    elif score >= 25:
        print("E")
    else:
        print("F")
