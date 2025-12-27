v = int(input("enter the wind velocity: "))
t = int(input("enter the temperature in fahrenheit: "))

if 50 < abs(t) or 120 < abs(v) < 3:
    wind_speed = 35.74 + 0.6215*t + (0.4275*t - 35.75)* (v**0.16)
    print("Wind speed is:", wind_speed)

else:
    print("Invalid input")