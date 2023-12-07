a, b = map(int, input().split())
go = [(1, 0), (0, 1)]
answer = 0

def search(i, j):
    global answer

    if i > j:
        return

    if i > b or j > b:
        return

    if (i, j) == (b, b):
        answer += 1
    
    for go_y, go_x in go:
        search(i+go_y, j+go_x)

search(a, a)

print(answer)