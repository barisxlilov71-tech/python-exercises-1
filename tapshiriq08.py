m=int(input())
if m<0:
    print("Invalid purchase amount")
elif m<100:
    print("No discount")
elif m<300:
    print(m,m*(0,1),m*(0,9))
elif m<500:
    print(m,m*(0,15),m*(0,85))
else:
    print(m,m*(0,2),m*(0,8))