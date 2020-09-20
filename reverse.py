# . A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895
num=int(input("enter 4 digit number"))
if num>1000:
    rev=num//1000
    num=num%1000
    rev+= (num//100)*10
    num= num%100
    rev+= (num//10)*100
    num=num%10
    rev+= (num)*1000
    print(rev)
else:
    print("enter number greater than 1000")