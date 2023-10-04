n = int(input())
coordinates = sorted(map(int, input().split()))
dp = [0] * n
dp[1] = coordinates[1] - coordinates[0]
if n == 2:
    print(dp[1])
else:
    dp[2] = coordinates[2] - coordinates[0]
    for i in range(3, n):
        dp[i] = coordinates[i] - coordinates[i - 1] + min(dp[i - 1], dp[i - 2])
    print(dp[n - 1])
