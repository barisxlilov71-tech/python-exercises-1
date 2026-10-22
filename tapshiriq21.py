PIN="0427"
pin=input("PIN is required: ")
if len(pin)!=4:
    print("PIN must have 4 digits")
elif not (pin.isdecimal()):
    print("Digits only")
elif pin==PIN:
    print("Access granted")
else:
    print("Incorrect PIN")