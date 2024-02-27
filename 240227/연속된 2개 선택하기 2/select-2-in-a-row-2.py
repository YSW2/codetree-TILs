n = int(input())
dp = [float(input())]

for i in range(1, n):
    num = float(input())
    dp.append(max(dp[i-1]*num, num))

answer = max(dp)
print(f"{answer:.3f}")