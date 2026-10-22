t=2
j=3
c=4
q=int(input())
code=input()
if (q>10 or q<1)or(code!=t and code!=j and code!=c):
    print("Error")
match code:
    case 2:
        if q*t>=20:
            print("Large order")
        else:
            print("Regular order")
        print(tea,q,q*t)
    case 3:
        if q*j>=20:
            print("Large order")
        else:
            print("Regular order")
        print(juice,q,q*j)
    case 4:
        print(coffee,q,q*c)
        if q*c>=20:
            print("Large order")
        else:
            print("Regular order")