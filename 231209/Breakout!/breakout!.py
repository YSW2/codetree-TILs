import copy

n = int(input())
arr = list(map(int, input().split()))
arr2 = copy.copy(arr)

if arr[0] > 0:
    print(-1)

else:
    idx = 0
    val = 0
    while idx < len(arr):
        if arr[idx] > -1:
            temp = arr[idx]
            temp_idx = idx
            while temp >= 0 and temp_idx >= 0:
                arr[temp_idx] = temp
                arr2[temp_idx] = temp
                temp_idx -= 1
                temp -= 1
            val = arr[idx]
            idx += 1
                
        else:
            arr2[idx] = 0
            arr[idx] = val
            val += 1
            idx += 1

    print(arr.count(0), arr2.count(0))