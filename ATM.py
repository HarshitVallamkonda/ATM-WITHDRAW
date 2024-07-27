#If you are Inserting Card To should give c in First Step
#The amount is fixed 1000

while True:
    account=10000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome jaya")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                                  1.balance enq
                                  2.withdraw'''))
            if option==1:
                       print("your acc balance is",account)
            elif option==2:
                       money=int(input("enter the amount"))
                       print(money)
                       balance=account-money
                       print("your remaining amout is",balance)
        else:
            print("incorrect password")
    else:
        print("invalid card")