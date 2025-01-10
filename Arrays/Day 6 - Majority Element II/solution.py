def findMajority(arr):
    n = len(arr) // 3
    elm1, elm2 = -1, -1
    cnt1, cnt2 = 0, 0

    for elm in arr:
        if elm1 == elm:
            cnt1 += 1
        elif elm2 == elm:
            cnt2 += 1
        elif cnt1 == 0:
            elm1 = elm
            cnt1 += 1
        elif cnt2 == 0:
            elm2 = elm
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    res = []
    cnt1, cnt2 = 0, 0

    for elm in arr:
        if elm1 == elm:
            cnt1 += 1
        elif elm2 == elm:
            cnt2 += 1

    if cnt1 > n:
        res.append(elm1)
    if cnt2 > n:
        res.append(elm2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res



arr = [4, 2, 4, 4, 5]
majority = findMajority(arr)  # [5, 6]
print(majority)
