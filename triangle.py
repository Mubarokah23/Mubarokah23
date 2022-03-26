a = input("Enter first side : ")
a = int(a)
b = input("Enter second side : ")
b = int(b)
c = input("Enter third side : ")
c = int(c)

if a == b and b == c :
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")