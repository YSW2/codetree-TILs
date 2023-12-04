a, b = map(int, input().split())
loc = a
go = 1
answer = 0

while True:
    move = abs(a + go - loc)
    loc = a + go
    answer += move
    if abs(loc-a) >= abs(b-a):
        answer -= abs(loc - b)
        break
    go *= -2

print(answer)