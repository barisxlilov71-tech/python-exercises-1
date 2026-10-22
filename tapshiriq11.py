eusage=float(input())
first=0.08
second=0.12
third=0.15
if eusage<0:
    print("Invalid usage")
elif eusage<100:
    print(eusage,first,eusage*first)
elif eusage<300:
    print(eusage,second,eusage*second)
else:
    print(eusage,third,eusage*third)
