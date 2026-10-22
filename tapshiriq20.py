id=input()
k=0
c=""
for i in id:
    if int(i)>=0 and int(i)<=9:
        k+=1
    else:
        c=c+i
if k==8:
    print("Student ID accepted")
else:
    print("these letters are invalid,your ID must contain 8 ASCII digits,plese change these digits with 0 to 9 ASCII codes",c)