# 2. Write a program to find the maximum of three numbers stored in variables.
a = int(input("enter a number"))
b = int(input("enter another number"))
c = int(input("enter another number"))
if a>b :
    if a>c:
        print ("a is the greatest")
    else:
        print("c is the greatest")
elif b>c:
    print("b is the greatest")
else:
    print("c is the greatest") 