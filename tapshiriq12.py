distance=int(input())
sf=2
f1=0,7
f2=0,6
f3=0,5
if distance<0:
    print("Invalid distance")
elif distance<=5:
    t=distance*f1
    print(sf,t,sf+t)
elif distance<=15:
    t=distance*f2
    print(sf,t,sf+t)
else:
    t=distance*f3
    print(sf,t,sf+t)