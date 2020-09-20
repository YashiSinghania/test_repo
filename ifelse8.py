# Write a program to print the minimum number of Rupee notes needed to match a given
# amount. Available denominations of notes are 2000, 500, 100, 50.
# 1. For example, if the amount is 28,550, then you need 14 notes of 2000, 1 note of 500,
# and 1 note of 50. So the total number of notes is 14+1+1 = 16. 
# HINT: 6500 / 2000 gives you the number (3) of 2000 notes.
# HINT: 6500 % 2000 gives you the amount remaining (500) after giving 3 notes of 2000.
amt = int(input("enter the amount"))
tot= 0
# if amt>=2000:
#      a = (amt//2000) + ((amt %2000) //500)+(((amt%2000)%500)//100)+((((amt%2000)%500)%100)//50)
#      print(a)
if amt>=2000 :
    tot= amt//2000
    amt= amt%2000
if amt>= 500 :
    tot+=amt//500
    amt= amt%500
if amt>= 100 :
    tot+=amt//100
    amt= amt%100
if amt >= 50:
    tot += amt // 50
    amt = amt % 50
print (tot)