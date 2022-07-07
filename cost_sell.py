#To find profit based on cost price and sell price of an item.

cost = float(input("please enter actual cost amount :-"))
sale = float(input("please enter sell amount :-"))

if (cost > sale):
    amount = cost - sale
    print("total loss amount = ", amount)
elif (sale > cost):
    amount = sale - cost
    print("total profit amount = ", amount)
else:
    print("no profit or no loss !!!")
