N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N+1)]
dp[1] = costs[0]
    
for i in range(2, N + 1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2]
    
print(min(dp[N]))