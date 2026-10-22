a=int(input())
b=int(input())
c=int(input())
d=0
if a+b>c:
    d+=1
    if a+c>b:
        d+=1
        if b+c>a:
            d+=1
if d==3:
    if a==b:
        if b==c:
            print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Triangle cannot be created")