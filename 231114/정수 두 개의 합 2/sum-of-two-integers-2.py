n, k = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] + arr[j] <= k:
            answer += 1

print(answer)