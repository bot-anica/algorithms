def getSecondLargest(arr):
    # Code Here
    max_number = arr[0]
    next_to_max_number = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_number:
            next_to_max_number = max_number
            max_number = arr[i]

        elif next_to_max_number < arr[i] < max_number:
            next_to_max_number = arr[i]

    return next_to_max_number


print(getSecondLargest([2, 3, 6, 6, 5]))
