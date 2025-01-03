# Reverse an Array

Difficulty: **Medium**

---
Given an array `arr[]`.
Rotate the array to the left (counter-clockwise direction) by `d` steps,
where `d` is a positive integer. Do the mentioned change in the `array in place`.

Note: Consider the array as circular.

### Examples
```commandline
Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
```
```commandline
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
```
```commandline
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
```

### Constraints

```commandline
1 <= arr.size(), d <= 10^5
```
```commandline
0 <= arr[i] <= 10^5
```