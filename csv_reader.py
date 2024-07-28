import csv


def csv_reader(file_name):
    with open(file_name, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [line for line in reader]
        return data
