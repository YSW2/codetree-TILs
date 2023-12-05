n = int(input())
dp = [0 for x in range(n)]

def recursive(n):
    if n <= 2:
        return 1
    
    elif n <= 4:
        return 2
    
    else:
        if dp[n] != 0:
            return dp[n]
        
        else:
            dp[n] = recursive(n-1) + recursive(n-5)
            return dp[n]

recursive(n-1)
print(dp[n-1])