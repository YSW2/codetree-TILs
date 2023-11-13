n, m = map(int, input().split())
arr = list(map(int, input().split()))

j = 1
arr_sum = arr[0]
answer = 0

for i in range(n):
    while j < n and arr_sum < m:
        arr_sum += arr[j]
        j += 1
    if arr_sum == m:
        answer += 1
    arr_sum -= arr[i]

print(answer)