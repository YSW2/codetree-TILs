n = int(input())
arr = list(map(int, input().split()))
answer = 0

j = 1
for i in range(n):
    while j < n and arr[j] not in arr[i:j]:
        j += 1
        answer = max(answer, j-i)
    i += 1

print(answer)