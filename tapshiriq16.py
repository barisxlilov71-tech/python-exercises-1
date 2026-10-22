es=int(input())
a=0
if es>100 or es<0:
    print("Invalid score")
else:
    while True:
        es+=1
        a+=1
        if es>=100 and a<50:
            print("Pass")
        else:
            print("Fail")