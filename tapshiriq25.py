ID=input()
age=input()
scode=input()
Payment=input()
if len(ID)!=8 or not (ID.isascii() and ID.isdecimal()):
    print("Invalid student ID")
elif not (age.isascii() and age.isdecimal()):
    print("Invalid age")
elif not 16<=int(age)<=65:
    ("Age must be between 16 and 65")
else:
    age=int(age)
    match scode:
        case "PY":
            name="Python Basics"
            price=30
            minage=16
        case "WEB":
            name="Web Development"
            price=40
            minage=16
        case "CY":
            name="Cyber Security"
            price=50
            minage=18
        case _:
            name=None
    if name==None:
        print("Invalid scode code")
    elif age<minage:
        print("Age is not enough")
    elif not (Payment.isascii()and Payment.isdecimal()):
        print("Invalid payment")
    else:
        if age<=18:
            finalfee=price*(0.2)
        else:
            finalfee=price
            paid=int(Payment)
            if paid<finalfee:
                print("Insufficient payment")
            else:
                print("Registration confirmed")
                print("Student ID:",ID)
                print("Workshop:",name)
                print("Final feeL:",finalfee,"AZN",sec=" ")
                print("Discount:",price*(0,2),"AZN",sec=" ")
