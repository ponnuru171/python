x=int(input("enter atm pin"))
balance=3000
if x == 9876:
    print("enter any choice to procede")
    c = int(input("""enter ur option
        1 for bal
        2 for credit
        3 for debit
        4 for exit
        """))
    if c == 1:
        print(balance)
    if c == 2:
        y=int(input("enter amount of money to add to account"))
        if y > 25000:
            print("the limit should be less than 25000")
        else:
            z=balance + y
            print(z)
    if c == 3:
        a=int(input("enter amount to withdraw"))
        if a > balance:
            print("infucient balance")
        else:
            b=balance - a
            print(b)
    if c == 4:
        exit()
    else:
        print("invalid number ur choice")
else:
    print("login failed enter correct pin")
