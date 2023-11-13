n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = n
arr_sum = arr[0]
j = 1

for i in range(n):
    while j < n and arr_sum < s:
        arr_sum += arr[j]
        j += 1
    
    if arr_sum >= s:
        answer = min(answer, j-i)

    arr_sum -= arr[i]


print(answer)