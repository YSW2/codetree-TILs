n = int(input())
record = []
cow = {"Bessie": 7, "Elsie": 7, "Mildred": 7}
board = ["Bessie", "Elsie", "Mildred"]
answer = 0

for _ in range(n):
    day, name, score = input().split()
    record.append([int(day), name, int(score)])

record.sort()
    
for day, name, score in record:
    cow[name] += score
    board_temp = [n for n, s in list(cow.items()) if s >= max(cow.values())]
    if board != board_temp:
        answer += 1
        board = board_temp

print(answer)