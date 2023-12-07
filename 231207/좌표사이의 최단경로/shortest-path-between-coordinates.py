a, b = map(int, input().split())
go = [(1, 0), (0, 1)]
answer = 0

s = min(a, b)
f = max(a, b)

def search(i, j):
    global answer

    if i > j:
        return

    if i > f or j > f:
        return

    if (i, j) == (f, f):
        answer += 1
    
    for go_y, go_x in go:
        search(i+go_y, j+go_x)

search(s, s)

print(answer)