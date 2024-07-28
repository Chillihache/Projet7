class Action:
    def __init__(self, name, cost, percentage_profit):
        self.name = name
        self.cost = float(cost)
        self.percentage_profit = float(percentage_profit)
        self.profit = cost * percentage_profit / 100


