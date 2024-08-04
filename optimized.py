import csv


class Action:
    def __init__(self, name, cost, percentage_profit):
        self.name = name
        self.cost = float(cost)
        self.percentage_profit = float(percentage_profit)
        self.profit = cost * percentage_profit / 100


class ActionManager:
    def __init__(self, data):
        self.data = data
        self.max_budget = 0
        self.actions = []
        self.best_profit = 0
        self.best_combination = []
        self.best_combination_cost = 0

    def create_actions_list(self):
        for i in range(len(self.data)):
            self.actions.append(Action(self.data[i]["name"],
                                       float(self.data[i]["price"]),
                                       float(self.data[i]["profit"])))

    def ask_budget(self):
        print("")
        while True:
            try:
                self.max_budget = round(float(input("Votre budget maximum : ")))
                if self.max_budget > 0:
                    return
                else:
                    print("Le budget ne peut pas être nul ou négatif")
            except ValueError:
                print("Veuillez entrer un nombre.")

    def knapsack(self):
        dp = [[0] * (int(self.max_budget + 1)) for _ in range(len(self.actions) + 1)]

        for i in range(1, len(self.actions) + 1):
            action = self.actions[i - 1]
            for j in range(int(self.max_budget + 1)):
                if action.cost <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][round(j - action.cost)] + action.profit)
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(len(self.actions), 0, -1):
            if dp[i][int(self.max_budget)] != dp[i - 1][int(self.max_budget)]:
                self.best_combination.append(self.actions[i - 1])
                self.best_profit += self.actions[i - 1].profit
                self.max_budget -= self.actions[i - 1].cost

        self.best_combination.reverse()
        self.best_combination_cost = sum(action.cost for action in self.best_combination)

    def show_best_combination(self):
        print("")
        print("Voici la meilleure combinaison possible :")
        print("")
        for action in self.best_combination:
            print(action.name)
        print("")
        print(f"Le cout total de ces actions est de : {round(self.best_combination_cost, 2)} euros")
        print(f"Le profit en deux ans sera de environ : {round(self.best_profit, 2)} euros")


def csv_reader(file_name):
    with open(file_name, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [line for line in reader]
        return data


def clean_data(data):
    cleaned_data = []
    for action in data:
        try:
            action["price"] = float(action["price"])
            action["profit"] = float(action["profit"])
            if action["price"] > 0 and action["profit"] > 0:
                cleaned_data.append(action)
        except (ValueError, TypeError):
            continue
    return cleaned_data


if __name__ == "__main__":

    data = csv_reader("datas/dataset2_Python+P7.csv")
    data = clean_data(data)
    action_manager = ActionManager(data)
    action_manager.create_actions_list()
    action_manager.ask_budget()
    action_manager.knapsack()
    action_manager.show_best_combination()
