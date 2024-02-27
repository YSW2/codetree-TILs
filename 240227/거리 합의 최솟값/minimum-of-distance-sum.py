n = int(input())
answer = 0
x_coord = []
y_coord = []

for _ in range(n):
    coord = input().split()
    x_coord.append(int(coord[0]))
    y_coord.append(int(coord[1]))

x_coord.sort()
y_coord.sort()

median_x = x_coord[len(x_coord) // 2]
median_y = y_coord[len(y_coord) // 2]

for i in range(n):
    answer += abs(median_x - x_coord[i])
    answer += abs(median_y - y_coord[i])

print(answer)