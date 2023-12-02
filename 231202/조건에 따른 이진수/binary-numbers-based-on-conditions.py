answer = 0
n = int(input())

def search(arr, n):
    global answer
    if len(arr) >= n:
        answer += 1
        return

    if len(arr) == 0:
        arr.append(1)
        search(arr, n)
        arr.pop()
    elif arr[-1] == 1:
        arr.append(0)
        search(arr, n)
        arr.pop()
    else:
        for i in range(2):
            arr.append(i)
            search(arr, n)
            arr.pop()

search([], n)
print(answer)