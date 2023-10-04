def solve(N):
    dp = [0] * N
    dp[0] = 2
    if N == 1:
        return dp[0]
    dp[1] = 4
    if N == 2:
        return dp[1]
    dp[2] = 7
    if N == 3:
        return dp[2]

    for i in range(3, N):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[-1]


N = int(input())
print(solve(N))