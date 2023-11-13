n, k = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(n-1, 0, -1):
    if arr[i] + arr[i-1] <= k:
        break

index = i
j = index - 1
answer = (j+1)*j // 2

for i in range(index, n):
    while j > 0 and arr[j] + arr[i] > k:
        j -= 1
    if arr[j] + arr[i] <= k:
        answer += j+1

print(answer)