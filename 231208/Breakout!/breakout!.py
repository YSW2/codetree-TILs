n = int(input())
arr = list(map(int, input().split()))
answer = [float("inf"), 0]

def search(arr2, i):
    global answer

    if arr[i] >= 0 and arr[i] != arr2[i]:
        return

    if i == len(arr)-1:
        val = arr2.count(0)
        answer[0] = min(val, answer[0])
        answer[1] = max(val, answer[1])

        return

    arr2.append(0)
    search(arr2, i+1)
    arr2.pop()

    arr2.append(arr2[i]+1)
    search(arr2, i+1)
    arr2.pop()

if arr[0] > 0:
    print(-1)

else:
    search([0], 0)
    if answer[1] > 0:
        print(answer[0], answer[1])
    else:
        print(-1)