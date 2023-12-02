answer = 0
n = int(input())

def search(arr, i):
    global answer
    if i == len(arr):
        answer += 1
        return
    
    if arr[i-1] == 0:
        arr[i] = 1
        search(arr, i+1)
        arr[i] = 0
        search(arr, i+1)
    else:
        search(arr, i+1)

arr = [0 for x in range(n)]
arr[0] = 1
search(arr, 1)
print(answer)