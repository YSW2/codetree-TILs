n = int(input())
record = []
cow = {"Bessie": 7, "Elsie": 7, "Mildred": 7}
board = ["Bessie", "Elsie", "Mildred"]
answer = 0

for _ in range(n):
    record.append(list(input().split()))

record.sort(key=lambda x:x[0])

for day, name, score in record:
    score = int(score[1]) * (1 if score[0] == '+' else -1)
    cow[name] += score

    board_temp = [n for n, s in list(cow.items()) if s >= max(cow.values())]
    if board != board_temp:
        answer += 1
        board = board_temp

print(answer)