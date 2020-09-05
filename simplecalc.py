# a=20
# b=30
# print(type(a))
# print(type(b))
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
# print(type(a))
# print(type(b))

op=input('enter operand')
if op== "+":
    result=int(a)+int(b)
elif op== "-":
    result=int(a)-int(b)
elif op== "/":
    result=int(a)//int(b)
elif op== "*":
    result=int(a)*int(b)
else:
    result="error"
print(result)




