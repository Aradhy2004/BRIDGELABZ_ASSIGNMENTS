import random
n = int(input("Enter number of coin flips:"))

heads =0 
tails =0
for _ in range(n):
    if random.random()<0.5:
        heads +=1
    else:
        tails +=1

print("Heads:", heads * 100 /n, "%")
print("Tails:", tails * 100 /n, "%")