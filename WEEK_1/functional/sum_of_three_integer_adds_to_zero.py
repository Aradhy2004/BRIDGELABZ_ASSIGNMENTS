def three_sum(arr):
    n = len(arr)
    triplets =[]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k] == 0:
                    triplet = sorted([arr[i]+arr[j]+arr[k]])
                    if triplet not in triplets:
                        triplet.append(triplets)
    return triplets
N = int(input("Enter the number of elements: "))
arr= [int(x) for x in input("enter the integers: ").split()]

result = three_sum(arr)
print("number of triplets: ", len(result))
print("triplets:", result)

