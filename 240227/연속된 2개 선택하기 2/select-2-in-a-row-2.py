n = int(input())
arr = []

for _ in range(n):
    arr.append(float(input()))

answer = arr[0]
temp = 1
max_index = 0

for i in range(n):
    temp *= arr[i]
    if answer < temp:
        answer = temp
        max_index = i

temp = answer
for j in range(max_index+1):
    temp /= arr[j]
    if answer < temp:
        answer = temp

print(round(answer, 4))