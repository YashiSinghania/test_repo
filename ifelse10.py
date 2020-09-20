# 10. Write a program to check whether the triangle is an equilateral, isosceles or scalene
# triangle. (Equilateral triangle has all  3 sides equal. An isosceles triangle has 2 sides equal. A
# scalene triangle has no side equal).
a= int(input("first side of triangle"))
b= int(input("second side of triangle"))
c= int(input("third side of triangle"))
if a == b == c :
    print("equilateral triangle")
elif a==b or b==c or c==a :
    print("isos triangle")
else:
    print("scalene triangle")
