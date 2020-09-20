#make a simple calculator by giving values to 2 variables from user input#
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
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