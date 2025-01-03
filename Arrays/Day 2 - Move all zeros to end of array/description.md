# Move All Zeroes to End

Difficulty: **Easy**

---
You are given an array `arr[]` of non-negative integers.
Your task is to move all the zeros in the array to the right end
while maintaining the relative order of the non-zero elements.
The operation must be performed `in place`,
meaning you should not use extra space for another array.

### Examples
```commandline
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
```
```commandline
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
```
```commandline
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
```

### Constraints

```commandline
1 ≤ arr.size() ≤ 10^5
```
```commandline
0 ≤ arr[i] ≤ 10^5
```