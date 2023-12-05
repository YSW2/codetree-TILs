import sys
sys.setrecursionlimit(10**4)

n = int(input())
answer = float("inf")

def dfs(arr, n):
    global answer

    if n <= 0:
        if n == 0:
            answer = min(len(arr), answer)
        return
    
    if n >= 7:
        arr.append(7)
        dfs(arr, n-7)

    elif n >= 5:
        arr.append(5)
        dfs(arr, n-5)
    
    else:
        for i in range(1, 3):
            arr.append(i)
            dfs(arr, n-i)
            arr.pop()

dfs([], n)
print(answer)