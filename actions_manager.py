from action import Action
import itertools


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
            self.actions.append(Action(self.data[i]["name"], float(self.data[i]["price"]), float(self.data[i]["profit"])))

    def find_valid_combinations(self):
        for i in range(1, len(self.actions) + 1):
            for combination in itertools.combinations(self.actions, i):
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

    def show_best_combination(self):
        print("")
        print("Voici la meilleure combinaison possible :")
        print("")
        for action in self.best_combination:
            print(action.name)
        print("")
        print(f"Le cout total de ces actions est de : {self.best_combination_cost}")
        print(f"Le profit en deux ans sera de environ : {round(self.best_profit, 2)} euros")