# triangle type
side = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side == side2 and side2 == side3:
    print("Equilateral")
elif side != side2 and side2 != side3 and side != side3:
    print("Scalene")
else:
    print("Isosceles")
