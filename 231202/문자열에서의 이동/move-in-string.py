n = int(input())
arr = list(input())
dp = [0 for x in range(n)]

def find_near(arr, i):
    string = ['c', 'b', 'a']
    target = (string.index(arr[i])+1)%3
    min_val = float("inf")
    count = 0

    while i >= 0:
        if arr[i] == string[target] and dp[i] != -1:
            min_val = min((dp[i] + count ** 2), min_val)
        i -= 1
        count += 1
    
    if min_val == float("inf"):
        return -1

    else:
        return min_val


for i in range(1, n):
    val = find_near(arr, i)
    dp[i] = val

print(dp[n-1])