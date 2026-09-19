#Sort three numbers in ascending and descending order using conditional statements.


a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))


print("Ascending Order : ",end="")
if a>b and a>c and b>c:
    print(c,b,a)
elif a>b and a>c and b<c:
    print(b,c,a)
elif a<b and b>c and a>c:
    print(c,a,b)
elif a<b and b>c and a<c:
    print(a,c,b)
elif c>a and b<c and a>b:
    print(b,a,c)
elif c>a and b<c and a<b:
    print(a,b,c)


print("Descending Order : ",end="")
if a>b and a>c and b>c:
    print(a,b,c)
elif a>b and a>c and b<c:
    print(a,c,b)
elif a<b and b>c and a>c:
    print(b,a,c)
elif a<b and b>c and a<c:
    print(b,c,a)
elif c>a and b<c and a>b:
    print(c,a,b)
elif c>a and b<c and a<b:
    print(c,b,a)
