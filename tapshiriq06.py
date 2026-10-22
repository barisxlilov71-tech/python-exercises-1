a=float(input())
b=float(input())
c=input()
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "**":
        if (a==0 and b<0) or (a<0 and not b.is_integer()):
            print("invalid operation")
        else:
            print(a**b)
    case "/":
        if b==0:
            print("invalid operation")
        else:
            print(a/b)
    case "%":
        if b==0:
            print("invalid operartion")
        else:
            print(a%b)
    case "//":
        if b==0:
            print("invalid operation")
        else:
            print(a//b)
    case "_":
        print("invalid operation")

