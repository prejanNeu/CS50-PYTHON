due=50
while True:
    if due > 0:
        print("Amount Due: "+str(due))
        coin =int(input("Insert Coin:"))
        if coin==25 or coin== 10 or coin ==5:
            if due>0:
                due=due-coin
    else:
            print("Change Owed: "+str(abs(due)))
            break