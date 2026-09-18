from math import pi
h = float(input("Enter Height : "))
r = float(input("Enter Radius : "))

print("Surface Volume = ",round(pi*r*r*h,2))
print("Total Surface Area = ",round((2*pi*r*(r+h)),2))
