def maximumProfit(prices):
    n = len(prices)
    minPrice = prices[0]
    res = 0

    for i in range(1, n):
        minPrice = min(minPrice, prices[i])
        res = max(res, prices[i] - minPrice)

    return res


if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maximumProfit(prices))
