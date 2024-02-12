def calcul(a, t, b):
    if t == "+":
        return a + b
    elif t == "-":
        return a - b
    elif t == "x":
        return a * b

n = int(input())
arr = []
go = [(0, 1), (1, 0)]
ans_min = float("inf")
ans_max = float("-inf")
x, y = 0, 0

for _ in range(n):
    arr.append(list(input().split()))

def dfs(x, y, calc):
    if len(calc) == 3:
        calc = [calcul(int(calc[0]), calc[1], int(calc[2]))]

    if x == n-1 and y == n-1:
        global ans_min
        global ans_max

        ans_min = min(ans_min, calc[0])
        ans_max = max(ans_max, calc[0])
        
        return
            
    for go_y, go_x in go:
        if y+go_y < n and x+go_x < n:
            calc.append(arr[y+go_y][x+go_x])
            dfs(x+go_x, y+go_y, calc)
            calc.pop()
        
dfs(0, 0, [arr[0][0]])
print(ans_max, ans_min)