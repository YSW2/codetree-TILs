n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = arr[n-1]

j = n-1
for i in range(n):
    if i == j:
        break
    answer = min(abs(arr[i]+arr[j]), answer)
    while j > i and arr[i] + arr[j] > 0:
        j -= 1
        answer = min(abs(arr[i]+arr[j]), answer)

print(answer)