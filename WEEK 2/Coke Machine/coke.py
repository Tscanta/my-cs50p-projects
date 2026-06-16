#COKE MACHINE!

amt_due = int(50) #initial due amount

while(amt_due > 0):
    print("Amount Due:",amt_due)
    coin = int(input("Insert Coin: "))

    if coin in [25,10,5]:
        amt_due -= coin

print("Change Owed:",abs(amt_due))
