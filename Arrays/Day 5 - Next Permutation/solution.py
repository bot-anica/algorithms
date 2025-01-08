def nextPermutation(arr):
    n = len(arr)
    target_index = -1

    # Array has Next Permutation if during getting each item in it from end one of them is lower then previous

    # Find target index
    for i in range(1, n):
        if arr[n - 1 - i] < arr[n - 1 - i + 1]:
            target_index = n - 1 - i
            break

    # Reverse array if target_index was not found
    if target_index == -1:
        for i in range(n // 2):
            arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

    # Else get Next Permutation
    else:
        # Replace number with target index and next higher number
        for i in range(0, n - 1 - target_index):
            if arr[target_index] < arr[n - 1 - i]:
                arr[target_index], arr[n - 1 - i] = arr[n - 1 - i], arr[target_index]
                break

        # Reverse all numbers after target index
        start = target_index + 1
        end = n - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    return arr


arr = [3, 2, 1]  # [2, 4, 5, 7, 0, 1]
nextPermutation(arr)  # [2, 4, 5, 0, 1, 7]
print(arr)
