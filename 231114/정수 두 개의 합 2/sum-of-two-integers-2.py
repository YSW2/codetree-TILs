n, k = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(1, n):
    if arr[0] + arr[i] > k:
        break

index = i-1

j = 0
for i in range(index, 0, -1):
    if i < j:
        break
    while j < i and arr[i] + arr[j] <= k:
        j += 1
    if arr[i] + arr[j-1] <= k:
        answer += j
    
print(answer)