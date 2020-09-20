# 6. Take input of age of 3 people by user and determine oldest and youngest among them.
a = int(input("enter age"))
b = int(input("enter age"))
c = int(input("enter age"))
if a>b :
    if a>c:
        print ("a is the eldest")

    else:
        print("c is the eldest")
        print("b is youngest")

if b > c :
    print("b is the eldest")
    print("c is the youngest")
else:
    print('c is the eldest')
    print('a is the youngest')
