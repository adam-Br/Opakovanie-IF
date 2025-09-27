a = float(input("dolná hranica intervalu: "))
b = float(input("horná hranica intervalu: "))

if a > b:
    print("dolná hranica intervalu musí byť mensia ako horná hranica intervalu, genius")
    exit()

x = float(input("x: "))

if x < a or x > b:
    print("číslo x nepatrí do intervalu  <a,b>")
else:
    print("číslo x patrí do intervalu  <a,b>")