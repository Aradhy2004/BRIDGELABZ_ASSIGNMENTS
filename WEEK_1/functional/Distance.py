x = int(input("enter x coordinate: "))
y = int(input("enter y coordinate: "))

distance = ((x * x) + (y * y)) ** 0.5
print("distance from (", x, "," , y, ") to the origin is ", distance)