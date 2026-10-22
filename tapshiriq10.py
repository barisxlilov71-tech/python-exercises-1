balance=1000
amount=float(input())
if amount<=0:
    print("Invalid amount")
elif amount>1000:
    print("Insufficient balance")
else:
    balance=balance-amount
    print(balance)