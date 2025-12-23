import random
def coupon_collection(n):
    collected = set()
    count = 0
    while(len(collected)<n):
        coupon = random.randint(1, n)
        count += 1
        collected.add(coupon)
    return count
n = int(input("Enter the number of distinct coupons: "))
result = coupon_collection(n)
print("Total random numbers generated to collect all coupons:", result)