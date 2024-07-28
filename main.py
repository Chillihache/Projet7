from csv_reader import csv_reader
from actions_manager import ActionManager
from clean_data import clean_data
from optimized import knapsack


"""
data = csv_reader("limited_data.csv")
data = clean_data(data)
actions_manager = ActionManager(data)
actions_manager.create_actions_list()
actions_manager.ask_budget()
actions_manager.find_valid_combinations()
actions_manager.find_best_combination()
actions_manager.calculate_best_combination_cost()
actions_manager.show_best_combination()
"""

data = csv_reader("dataset2_Python+P7.csv")
data = clean_data(data)
action_manager = ActionManager(data)
action_manager.create_actions_list()


actions = []
for action in action_manager.actions:
    actions.append((action.cost, action.profit))

print(len(actions))

results = knapsack(actions, 500)

print(results)

print(sum(result[0] for result in results[1]))






