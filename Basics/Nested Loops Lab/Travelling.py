while True:
    destination = str(input())
    if destination == "End":
        break
    minimal_budget_for_traveling = float(input())
    collected_money = 0

    while True:
        current_sum = float(input())
        collected_money += current_sum
        if collected_money >= minimal_budget_for_traveling:
            break

    if collected_money >= minimal_budget_for_traveling:
        print(f'Going to {destination}!')

