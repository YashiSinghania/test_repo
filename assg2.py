# 3. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
rate =int(input('enter the rate of the product'))
quantity=int(input("enter the quantity"))
if rate*quantity>1000:
    amt= (rate*quantity)*(0.9)
else:
    amt= (rate*quantity)
print(amt)