n = int(input())
arr = []
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

def greedy(n, arr, day, pay):
    global answer

    if day >= n:
        if day == n:
            answer = max(answer, pay)
        return
    
    for i, (t, p) in enumerate(arr):
        greedy(n, arr[i+t:], day+i+t, pay+p)

    greedy(n, arr, n, pay)

greedy(n, arr, 0, 0)
print(answer)