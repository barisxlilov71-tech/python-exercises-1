balance=1000
PIN="0427"
pin=input("PIN is required: ")
amount=int(input())
if pin==PIN and 10<=amount<=500:

    if amount%10==0:
        if amount<=200:
            fee=0
            z=balance-amount-fee
            print(amount,fee,z)
        else:
            fee=2
            z=balance-amount-fee
            print(amount,fee,z)
    else:
        print("Invalid amount")
else:
    print("Invalid PIN or amount")