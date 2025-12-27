n=int(input("Enter a number: "))
def harmonic(n):
    if n == 0:
        return 0
    else:
        return sum(1/n for n in range(1, n+1))
result = harmonic(n)
print(f"The {n}th harmonic number is: {result}")
