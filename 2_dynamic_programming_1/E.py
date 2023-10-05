def sum_half_game_stories(team1_score, team2_score):
    # Calculate the sum of the first half game stories, assuming that the start score was 0 : 0
    team1_score += 1
    team2_score += 1

    dp = [[0] * team2_score for _ in range(team1_score)]
    dp[0][0] = 1

    for i in range(team1_score):
        for j in range(team2_score):
            # dp[i][j] = the sum of 3 previous values in row and column
            # the dp[i][j] = dp[i][j] need only for i==j==0
            previous3_row = [dp[i - k][j] if i - k >= 0 else 0 for k in range(4)]
            previous3_col = [dp[i][j - k] if j - k >= 0 else 0 for k in range(1, 4)]
            dp[i][j] = sum(previous3_row + previous3_col)

    return dp[-1][-1]


a, b = map(int, input().split())
c, d = map(int, input().split())
first_part = sum_half_game_stories(a, b)
second_part = sum_half_game_stories(c - a, d - b)
print(first_part * second_part)


