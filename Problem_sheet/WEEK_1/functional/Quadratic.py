# Quadratic equation solver in Python

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

delta = b*b - 4*a*c

if delta > 0:
    root1 = (-b + delta**0.5) / (2*a)
    root2 = (-b - delta**0.5) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
else:
    print("No real roots (complex roots exist)")
