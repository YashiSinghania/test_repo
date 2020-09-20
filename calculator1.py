#make a simple calculator by giving values to 2 variables using single assignment#
a = b = int(input("enter the number:"))
op = input('enter operand')
if op == "+":
    result = a+b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
elif op == "/":
    result = a/b
elif op == "//":
    result = a//b
elif op == "%":
    result = a % b
else:
    result = "error"
print(result)