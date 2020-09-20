# 4. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary = int(input("enter your salary"))
service =int(input("enter your years of service"))
if service>5 :
    bonus= 0.5*salary
else:
    bonus=0
print(bonus)
