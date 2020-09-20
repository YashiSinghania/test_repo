# Write a program that prints “YES” if a number is divisible by both 5 and 11, and prints
# “NO” otherwise.
num = int(input("enter a number"))
if num%5==0 and num%11==0:
    print("YES")
else :
    print("NO")