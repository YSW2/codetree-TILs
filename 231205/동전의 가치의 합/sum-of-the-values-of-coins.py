n = int(input())
coin = [1, 2, 5, 7]
answer = float("inf")
temp = 0

def dfs(arr, n):
    global answer

    if n <= 0:
        if n == 0:
            answer = min(len(arr), answer)
        return
    
    for c in coin:
        arr.append(c)
        dfs(arr, n-c)
        arr.pop()

if n > 100:
    temp = (n-100) // 7
    n -= temp * 7

dfs([], n)
print(answer+temp)