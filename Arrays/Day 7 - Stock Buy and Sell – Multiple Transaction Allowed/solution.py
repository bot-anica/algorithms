def maximumProfit(prices):
    n = len(prices)
    profit = 0

    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


prices = [4, 2, 2, 2, 4]
profit = maximumProfit(prices)  # 865
print(profit)
