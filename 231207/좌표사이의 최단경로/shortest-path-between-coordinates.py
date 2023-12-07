a, b = map(int, input().split())

s = min(a, b)
f = max(a, b)

dp = [[0 for x in range(f+1)] for x in range(f+1)]

dp[s][s] = 1

for i in range(s+1, f+1):
    dp[s][i] += dp[s][i-1]

for i in range(s+1, f+1):
    for j in range(s+1, f+1):
        if i > j:
            continue
        
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
print(dp[f][f])