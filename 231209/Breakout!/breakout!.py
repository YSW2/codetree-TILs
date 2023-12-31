import copy

n = int(input())
arr = list(map(int, input().split()))


def check(arr):
    for i in range(len(arr)):
        if i == 0 and arr[i] > 0:
            return False

        elif arr[i] > 0 and arr[i] - arr[i-1] != 1:
            return False
    
    return True

idx = 0

while idx < len(arr):
    if arr[idx] > -1:
        temp = arr[idx]
        temp_idx = idx
        
        while temp_idx >= 0 and temp >= 0:
            arr[temp_idx] = temp
            temp -= 1
            temp_idx -= 1

            if arr[temp_idx] >= 0:
                break
        
    idx += 1

arr2 = copy.copy(arr)

for i in range(len(arr)):
    if arr[i] == -1:
        arr[i] = 0

val = 0

for i in range(len(arr2)):
    if arr2[i] == -1:
        arr2[i] = val
        val += 1
    else:
        val = arr2[i] + 1

if check(arr):
    #print(arr, arr2)
    print(arr2.count(0), arr.count(0))

else:
    print(-1)