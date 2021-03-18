"""
    wt => arr of size of elems
    vals => profit of each elem
    W => size of bag
"""

def maximizeProfit(wt, val, W):
    dp = []
    for i in wt:
        dp.append([])
    dp.append([])
    
    for row in dp:
        for col in range(0, W+1):
            row.append(0)
    max_wt = 0
    for row in range(1, len(wt)+1):
        max_wt += wt[row-1]
        for col in range(1, W+1):
            if col > max_wt:
                dp[row][col] = dp[row-1][max_wt]
            else:
                dp[row][col] = max(dp[row-1][col], val[row-1]+dp[row-1][col-wt[row-1]])
    return dp[row][col]

print("Maximum profit with knapsack is", maximizeProfit([1,2,3], [10,15,40], 6)) #65
print("Maximum profit with knapsack is", maximizeProfit([10,20,30], [60, 100, 120], 50)) #220