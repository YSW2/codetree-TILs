n = int(input())
coin = [1, 2, 5, 7]
answer = float("inf")

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

dfs([], n)
print(answer)