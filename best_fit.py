# Example file: best_fit.py

# explanations for member functions are provided in requirements.py

def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = []  # List of remaining capacities

    for i, item in enumerate(items):
        min_index = -1
        min_remaining = float('inf')

        # Step 1: Find the tightest-fitting bin (minimal leftover space)
        for j, remaining in enumerate(bins):
            if item <= remaining:
                leftover = remaining - item
                if leftover < min_remaining:
                    min_remaining = leftover
                    min_index = j

        # Step 2: Place the item
        if min_index != -1:
            assignment[i] = min_index
            bins[min_index] = round(bins[min_index] - item, 2)
        else:
            assignment[i] = len(bins)
            bins.append(round(1.0 - item, 2))

    # Step 3: Output final free space
    free_space[:] = bins


def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    # Step 1: Sort items in decreasing order with original indices
    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])

    bins = []  # List of remaining capacities

    # Step 2: Run Best-Fit on sorted items
    for original_index, item in indexed_items:
        min_index = -1
        min_remaining = float('inf')

        for j, remaining in enumerate(bins):
            if item <= remaining:
                leftover = remaining - item
                if leftover < min_remaining:
                    min_remaining = leftover
                    min_index = j

        if min_index != -1:
            assignment[original_index] = min_index
            bins[min_index] = round(bins[min_index] - item, 2)
        else:
            assignment[original_index] = len(bins)
            bins.append(round(1.0 - item, 2))

    # Step 3: Final free space
    free_space[:] = bins
