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
    
    elif n >= 2:
        arr.append(2)
        dfs(arr, n-2)
    
    else:
        arr.append(1)
        dfs(arr, n-1)

dfs([], n)
print(answer)