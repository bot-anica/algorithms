# ? First variant
# def rotateArray(arr, d):
#     n = len(arr)
#     d = d % n
#
#     for i in range(d // 2):
#         arr[i], arr[d - 1 - i] = arr[d - 1 - i], arr[i]
#
#     for i in range(n // 2):
#         arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
#
#     for i in range((n - d) // 2):
#         arr[i], arr[n - d - 1 - i] = arr[n - d - 1 - i], arr[i]


# ? Second variant
# def rotateArray(arr, d):
#     n = len(arr)
#     d = d % n
#
#     reverseArrPart(arr, d)
#     reverseArrPart(arr, n)
#     reverseArrPart(arr, n - d)
#
#
# def reverseArrPart(arr, last_index):
#     for i in range(last_index // 2):
#         arr[i], arr[last_index - 1 - i] = arr[last_index - 1 - i], arr[i]


# ? Third variant
def rotateArray(arr, d):
    n = len(arr)
    d = d % n

    reverse(arr, 0, d - 1)
    reverse(arr, 0, n - 1)
    reverse(arr, 0, n - 1 - d)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5]
rotateArray(arr, 2)  # [3, 4, 5, 1, 2]
print(arr)
