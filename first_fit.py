
# Example file: first_fit.py

# explanations for member functions are provided in requirements.py

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = []  # List of remaining capacities

    for i, item in enumerate(items):
        # Step 1: Find first bin that fits the item
        bin_found = False
        for j, remaining in enumerate(bins):
            if item <= remaining:
                # Step 2a: Assign item to bin j
                assignment[i] = j
                bins[j] -= item
                bin_found = True
                break

        # Step 2b: If no bin fits, create a new one
        if not bin_found:
            bin_index = len(bins)
            assignment[i] = bin_index
            bins.append(1.0 - item)

    # Step 3: Output final free space
    free_space[:] = [round(cap, 2) for cap in bins]


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    # Step 1: Sort items in decreasing order, but remember original indices
    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])

    bins = []  # list of remaining capacities

    # Step 2: First-Fit on sorted items
    for original_index, item in indexed_items:
        placed = False
        for j, remaining in enumerate(bins):
            if item <= remaining:
                assignment[original_index] = j
                bins[j] -= item
                placed = True
                break

        if not placed:
            bin_index = len(bins)
            assignment[original_index] = bin_index
            bins.append(1.0 - item)

    # Step 3: Final free space output
    free_space[:] = [round(cap, 2) for cap in bins]
