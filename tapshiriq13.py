age=int(input())
monthlysalary=int(input())
requestedloan=int(input())
a=0
if age>=18:
    a+=1
    if monthlysalary>=500:
        a+=1
        if requestedloan<=monthlysalary*10:
            a+=1
            
if a==3:
    print("Loan is approved")
elif a==2:
    print("Loan is not approved,Reason:loan is above 10 times salary")
elif a==1:
    print("Loan is not approved,Reason:monthlysalary is below 500")
else:
    print("Loan is not approved,Reason:age is below 18")