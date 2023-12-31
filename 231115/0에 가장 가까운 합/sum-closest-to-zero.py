n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = float("inf")

j = n-1
for i in range(n):
    if i == j:
        break
    answer = min(abs(arr[i]+arr[j]), answer)
    while j > i and arr[i] + arr[j] > 0:
        answer = min(abs(arr[i]+arr[j]), answer)
        j -= 1
        
print(answer)