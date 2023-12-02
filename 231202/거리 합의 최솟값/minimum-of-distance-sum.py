n = int(input())
answer = 0
dot_list = []

for _ in range(n):
    dot_list.append(list(map(int, input().split())))

dot_x, dot_y = dot_list[0]

for d_x, d_y in dot_list[1:]:
    dot_x += d_x
    dot_y += d_y

dot_x //= n
dot_y //= n
for d_x, d_y in dot_list:
    answer += abs(dot_x - d_x) + abs(dot_y - d_y)

print(answer)