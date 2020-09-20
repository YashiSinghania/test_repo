# 6. Write a program to check whether a character is an uppercase or lowercase alphabet.
# Print “U” for uppercase and “L” for lowercase.
# HINT: You can compare two characters. Their ASCII codes will be compared.

alph =input("enter an apbhabet")
if alph >= "A" and alph <= "Z":
    print("U")
elif alph>="a" and alph <= "z":
    print("L")
else:
    print('invalid input')