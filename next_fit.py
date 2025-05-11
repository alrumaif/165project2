from decimal import Decimal, getcontext

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    getcontext().prec = 28 

    bin_capacity = Decimal('1.0')
    current_bin = 0
    remaining_capacity = bin_capacity

    for i, item in enumerate(items):
        item_decimal = Decimal(str(item))
        if item_decimal <= remaining_capacity:
            assignment[i] = current_bin
            remaining_capacity -= item_decimal
        else:
            free_space.append(float(remaining_capacity))
            current_bin += 1
            assignment[i] = current_bin
            remaining_capacity = bin_capacity - item_decimal

    free_space.append(float(remaining_capacity))