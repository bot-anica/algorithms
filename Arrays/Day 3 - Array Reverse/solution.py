def reverseArray(arr):
    n = len(arr)

    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]


arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)
