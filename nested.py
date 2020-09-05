# If you have Rs 50 with you, then check the price of apples and oranges. If apples are worth 30/kg and oranges are worth 20/kg then buy 1kg of each fruit, else buy grapes worth rs50. Otherwise buy Mangoes of whatever you have.

# cash=int(input("the amount of cash you have"))
# apples=int(input("the price of apples per kg"))
# oranges=int(input("the price of oranges per kg"))
# grapes=int(input("the price of grapes"))
# if cash==50:
#     if apples==30:
#         if oranges==20:
#             print("bought apples and oranges")
# elif grapes==50:
#     print("grapes bought")
# else:
#     print('mangoes bought')


# If you have Rs 50 with you, then check the price of apples and oranges. If apples are worth 30/kg and oranges are worth 20/kg then buy 1kg of each fruit, else buy grapes worth rs50. Otherwise buy Mangoes of whatever you have.

cash = int(input("How much money do you have? "))

if cash == 50:
    apples = int(input("Price of apples: "))
    oranges = int(input("Price of oranges: "))
    if apples == 30 and oranges == 20:
        print("Get 1kg of each fruit.")
    else:
        print("Give me grapes worth Rs. 50.")
else:
    print("Give me Mangoes of worth Rs. "+str(cash))