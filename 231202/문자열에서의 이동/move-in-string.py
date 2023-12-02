n = int(input())
arr = list(input())
dp = [0 for x in range(n)]

def find_near(arr, i):
    string = ['a', 'b', 'c']
    target = (string.index(arr[i])+1)%3
    while i < len(arr):
        if arr[i] == string[target]:
            return i
        i += 1

    return -1


for i in range(n-2, -1, -1):
    idx = find_near(arr, i)
    if idx == -1:
        dp[i] = -1
    else:
        dp[i] = dp[idx] + (idx-i) ** 2

print(dp[0])