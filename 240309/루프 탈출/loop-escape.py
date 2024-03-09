n = int(input())
arr = []
state = [0 for x in range(n)]

for _ in range(n):
    arr.append(int(input()))

for i, n in enumerate(state):
    temp = []
    if n == 0:
        index = i+1
        while True:
            temp.append(index)
            index = arr[index-1]
            if index in temp:
                for j in temp:
                    state[j-1] = -1
                break
            elif index == 0:
                for j in temp:
                    state[j-1] = 1
                break

print(state.count(1))