from math import sqrt
l = float(input("Rectangle length : "))
w = float(input("Rectangle width : "))

print("Area = ",l*w)
print("Diagonal = ",round(sqrt(l**2+w**2),2))
print("Perimeter = ",2*(l+w))
