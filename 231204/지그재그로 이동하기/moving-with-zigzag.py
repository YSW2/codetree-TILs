a, b = map(int, input().split())
b -= a
loc = 0
go = 1
answer = 0

while True:
    if abs(go) >= abs(b):
        answer += abs(loc - b)
        break
    answer += abs(go - loc)
    loc = go
    go *= -2
print(answer)