a, b = map(int, input().split())
b -= a
loc = 0
go = 1
answer = 0

while True:
    if b < 0 and go <= b or b >= 0 and b <= go:
        answer += abs(loc - b)
        break
    answer += abs(go - loc)
    loc = go
    go *= -2
print(answer)