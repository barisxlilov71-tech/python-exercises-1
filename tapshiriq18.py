a=int(input())
match a:
    case 1:
        print("Monday,Study day")
    case 2:
        print("Tuesday,Study day")
    case 3:
        print("Wednesday,Study day")
    case 4:
        print("Thursday,Study day")
    case 5:
        print("Friday,Study day")
    case 6:
        print("Satruday,Weekend")
    case 7:
        print("Sunday,Weekend")
    case _:
        print("Invalid day")