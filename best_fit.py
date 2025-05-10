# Example file: best_fit.py

# explanations for member functions are provided in requirements.py
from decimal import Decimal
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = []

    for i, item in enumerate(items):
        min_index = -1
        min_remaining = float('inf')

        for j, remaining in enumerate(bins):
            if item <= remaining:
                leftover = remaining - item
                if leftover < min_remaining:
                    min_remaining = leftover
                    min_index = j

        if min_index != -1:
            assignment[i] = min_index
            bins[min_index] = round(bins[min_index] - item, 2)
        else:
            assignment[i] = len(bins)
            bins.append(round(1.0 - item, 2))

    free_space[:] = bins




def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    # Clear assignment and free_space in case reused
    for i in range(len(items)):
        assignment[i] = -1
    free_space.clear()

    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])
    bins = []  # list of Decimal capacities

    for original_index, item in indexed_items:
        item_dec = Decimal(str(item))
        best_bin = -1
        min_leftover = Decimal('Infinity')

        for j, space in enumerate(bins):
            if item_dec <= space:
                leftover = space - item_dec
                if leftover < min_leftover:
                    min_leftover = leftover
                    best_bin = j

        if best_bin != -1:
            assignment[original_index] = best_bin
            bins[best_bin] -= item_dec
        else:
            new_bin = Decimal('1.0') - item_dec
            bins.append(new_bin)
            assignment[original_index] = len(bins) - 1

    free_space[:] = [float(b.quantize(Decimal('0.01'))) for b in bins]

