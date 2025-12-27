def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n//i
        else:
            i = i + 1
    if n > 1:   # leftover prime
        factors.append(n)
    return factors

n = int(input("Enter an integer: "))
print(f"The prime factors are: {prime_factors(n)}")

    

