a=int(input())
b=int(input())
c=int(input())
if a>b and a>c and b>c:
    print(c,b,a)
elif a>b and a>c:
    print(b,c,a)
elif b>a and b>c and a>c:
    print(c,a,b)
elif b>a and b>c:
    print(a,c,b)
elif c>a and c>b and a>b:
    print(b,a,c)
else:
    print(a,b,c)