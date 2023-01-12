weight = float(input("Weight: "))
unit = str(input("(K)g or (L)bs: "))

if unit.upper() == "K":
    convert = float(weight * 2.205)
    print("Weight in lbs: "+ str(convert))


else:
    convert = float(weight / 2.205)
    print("Weight in kgs: "+ str(convert))

