import copy

n = int(input())
arr = list(map(int, input().split()))
arr2 = copy.copy(arr)
no_answer = False

if arr[0] > 0:
    print(-1)

else:
    idx = 0
    val = 0
    while idx < len(arr):
        if no_answer:
            print(-1)
            break
        if arr[idx] > -1:
            temp = arr[idx]
            temp_idx = idx
            while temp >= 0 and temp_idx >= 0:
                if arr[temp_idx] != temp:
                    no_answer = True
                    break
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

    if not no_answer:
        print(arr.count(0), arr2.count(0))