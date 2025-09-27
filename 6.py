x = float(input("x: "))

if x == 0 or x%4 != 0 and x%7 != 0:
    print("číslo nie je delitelné štyrmi alebo siedmimi")
elif x%4 == 0:
    print("číslo je delitelné štyrmi")
elif x%7 == 0:
    print("číslo je delitelné siedmimi")
