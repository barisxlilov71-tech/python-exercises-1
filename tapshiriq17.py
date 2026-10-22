order=int(input())
membership=input()
fee=5
if order<0 or (membership!="yes" and membership!="no"):
    print("Error")
elif order>=50 or membership=="yes":
    print("fee is free",order)
else:
    print(fee,order+fee)