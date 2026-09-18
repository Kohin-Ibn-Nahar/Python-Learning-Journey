from math import pi
r = float(input("Enter Radius : "))
a = float(input("Enter Angle : "))

print("Arc Length = ",round((a/360)*2*pi*r,2))
print("Sector Area = ",round((a/360)*pi*r*r,2))
