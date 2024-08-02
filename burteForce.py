import csv
from itertools import combinations


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
        self.valid_combinations = []
        self.best_profit = 0
        self.best_combination = ()
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
                self.max_budget = float(input("Votre budget maximum : "))
                if self.max_budget > 0:
                    return
                else:
                    print("Le budget ne peut pas être nul ou négatif")
            except ValueError:
                print("Veuillez entrer un nombre.")

    def find_valid_combinations(self):
        for i in range(1, len(self.actions) + 1):
            for combination in combinations(self.actions, i):
                if sum(action.cost for action in combination) <= self.max_budget:
                    self.valid_combinations.append(combination)

    def find_best_combination(self):
        for combination in self.valid_combinations:
            profit = sum(action.profit for action in combination)
            if profit > self.best_profit:
                self.best_profit = profit
                self.best_combination = combination

    def calculate_best_combination_cost(self):
        self.best_combination_cost = sum(action.cost for action in self.best_combination)

    def show_best_combination(self):
        print("")
        print("Voici la meilleure combinaison possible :")
        print("")
        for action in self.best_combination:
            print(action.name)
        print("")
        print(f"Le cout total de ces actions est de : {self.best_combination_cost} euros")
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

    data = csv_reader("datas/limited_data.csv")
    data = clean_data(data)
    action_manager = ActionManager(data)
    action_manager.create_actions_list()
    action_manager.ask_budget()
    action_manager.find_valid_combinations()
    action_manager.find_best_combination()
    action_manager.calculate_best_combination_cost()
    action_manager.show_best_combination()
