es=int(input())
ss=int(input())
age=int(input())
if age<0 or es<0 or es>700 or ss<0 or ss>100:
    print("Invalid data")
elif age<16:
    print("Rejected,Reason:Your age is not enough")
elif es>=600:
    print("Scholarship")
elif es>=450:
    print("Accepted")
elif es>=300:
    if ss>=80:
        print("Accepted")
    else:
        print("Rejected,Reason:Your school score is not enough")
else:
    print("Rejected,Reason:Your exam score is not enough")

