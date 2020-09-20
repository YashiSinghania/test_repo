#make a simple calculator by giving values to 2 variables using multiple assignment#
a, b = 20, 30
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