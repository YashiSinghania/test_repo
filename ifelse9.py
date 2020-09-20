# Write a program to check if a triangle can be formed using the given lengths of 3 sides.
# HINT: For example, if the sides are 10, 24, and 67, then you cannot make a triangle
# because 10+24 is not greater than or equal to 67.

a= int(input("first side of triangle"))
b= int(input("second side of triangle"))
c= int(input("third side of triangle"))
if a+b>=c and b+c>=a and a+c>=b:
    print("triangle possible")
else:
    print("triangle not possible")