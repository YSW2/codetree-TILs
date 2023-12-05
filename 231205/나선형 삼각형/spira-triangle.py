n = int(input())
dp = [0 for x in range(n)]

def recursive(n):
    if dp[n] != 0:
        return dp[n]
    
    else:
        if n <= 2:
            dp[n] = 1
            return 1

        elif n <= 4:
            dp[n] = 2
            return 2

        else:
            dp[n] = recursive(n-1) + recursive(n-5)

recursive(n-1)
print(dp[n-1])