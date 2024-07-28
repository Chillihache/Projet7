def knapsack(actions, max_weight):
    scale = 100
    scaled_max_weight = int(max_weight * scale)
    scaled_actions = [(int(cost * scale), profit) for cost, profit in actions]

    n = len(scaled_actions)
    dp = [[0] * (scaled_max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost, profit = scaled_actions[i - 1]
        for w in range(scaled_max_weight + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + profit)
            else:
                dp[i][w] = dp[i - 1][w]

    w = scaled_max_weight
    chosen_actions = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_actions.append(actions[i - 1])
            w -= scaled_actions[i - 1][0]

    chosen_actions.reverse()
    return dp[n][scaled_max_weight], chosen_actions
