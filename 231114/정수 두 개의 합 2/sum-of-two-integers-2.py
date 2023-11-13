n, k = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    arr.append(int(input()))

arr.sort()

j = n - 2
for i in range(n-1, 0, -1):
    if i == j:
        j -= 1
    while j > 0 and arr[i] + arr[j] > k:
        j -= 1
    if arr[i] + arr[j] <= k:
        answer += j+1

print(answer)