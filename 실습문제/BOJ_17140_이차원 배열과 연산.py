from copy import deepcopy

r, c, k = map(int(input().split()))
arr = [list(map(int, input().split())) for _ in range(3)]
arr2 = deepcopy(arr)
count = 0
if arr[r][c] == k:
