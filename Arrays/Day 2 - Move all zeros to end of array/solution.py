def pushZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1


arr = [0, 0]
pushZerosToEnd(arr)
print(arr)
