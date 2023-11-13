n = int(input())
arr = list(map(int, input().split()))
visited = [0 for x in range(100001)]
answer = 0

j = 1
for i in range(n):
    while j < n and visited[arr[j]] < 1:
        visited[arr[j]] += 1
        answer = max(answer, j-i)
        j += 1

    visited[arr[i]] -= 1
    i += 1

print(answer)