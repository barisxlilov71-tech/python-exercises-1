number=input()
prefix=input()
k=len(number)
match prefix:
    case "050":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")
    case "051":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")
    case "055":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")
    case "070":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")
    case "077":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")
    case "099":
        if (number.isdecimal and k==10):
            print("Phone number accepted")
        else:
            print("Phone number rejected")