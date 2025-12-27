def read_2d_array(data_type):
    # Step 1: Take dimensions
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))

    # Step 2: Initialize empty 2D array
    arr = []

    print(f"Enter {m*n} values ({data_type}):")
    for i in range(m):
        row = []
        for j in range(n):
            val = input()
            # Convert based on type
            if data_type == "int":
                val = int(val)
            elif data_type == "float":
                val = float(val)
            elif data_type == "bool":
                val = val.lower() in ["true", "1", "yes"]
            row.append(val)
        arr.append(row)

    return arr

def print_2d_array(arr):
    print("2D Array:")
    for row in arr:
        print(" ".join(str(x) for x in row))

# Example usage
array = read_2d_array("int")   # choose "int", "float", or "bool"
print_2d_array(array)

