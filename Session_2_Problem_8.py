#Take input of age of 3 people by user and determine oldest and youngest among them.

a = float(input("Enter Age of First Person: "))
b = float(input("Enter Age of Second Person: "))
c = float(input("Enter Age of Third Person: "))

maxi = max(a,b,c)
mini = min(a,b,c)

if maxi == a:
    print("The Oldest One is : First Person")
elif maxi == b:
    print("The Oldest One is : Second Person")
elif maxi == c:
    print("The Oldest One is : Third Person")


if mini == a:
    print("The Youngest One is : First Person")
elif mini == b:
    print("The Youngest One is : Second Person")
elif mini == c:
    print("The Youngest One is : Third Person")
