n = int(input())
answer = 0

def dfs(arr, n):
    global answer
    
    if n <= 0:
        if n == 0:
            answer += 1
        return
    
    for i in range(1, 4):
        arr.append(i)
        dfs(arr, n-i)
        arr.pop()

dfs([], n)
print(answer)