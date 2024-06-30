n, x = map(int, input().split())
queue = list(map(int, input().split()))
out = [0 for _ in range(n)]
index = 0
answer = 0
cnt = 0

while True: 
    if queue[index] == max([queue[i] for i in range(n) if out[i] == 0]) and out[index] == 0:
        out[index] = 1
        answer += 1

    if out[x] == 1:
        break

    index += 1
    index %= n

print(answer)