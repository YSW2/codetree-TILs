n = int(input())
dp = [0 for x in range(n+1)]

def recursive(n):
    if dp[n] != 0:
        return dp[n]
    
    else:
        if n <= 3:
            dp[n] = 1
            return 1

        elif n <= 5:
            dp[n] = 2
            return 2

        else:
            dp[n] = recursive(n-1) + recursive(n-5)

recursive(n)
print(dp[n])