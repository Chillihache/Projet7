def clean_data(data):
    cleaned_data = []
    for action in data:
        try:
            action["price"] = float(action["price"])
            action["profit"] = float(action["profit"])
            if action["price"] > 0 and action["profit"] > 0:
                cleaned_data.append(action)
        except (ValueError, TypeError):
            # Ignorer les entrées qui ne peuvent pas être converties en float
            continue
    return cleaned_data
