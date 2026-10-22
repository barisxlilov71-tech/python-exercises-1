age=int(input())
if age<0:
    print("Invalid Age")
elif age<13:
    print("Child")
elif age<18:
    print("Teenager")
elif age<65:
    print("Adult")
else:
    print("Senior")