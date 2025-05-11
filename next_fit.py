from decimal import Decimal, getcontext

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    getcontext().prec = 28  

    bin_capacity = Decimal('1.0')
    current_bin = 0
    remaining = bin_capacity

    for i, item in enumerate(items):
        item_dec = Decimal(str(item))
        if item_dec <= remaining:
            assignment[i] = current_bin
            remaining -= item_dec
        else:
            free_space.append(float(remaining))
            current_bin += 1
            assignment[i] = current_bin
            remaining = bin_capacity - item_dec

    free_space.append(float(remaining))
