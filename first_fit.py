# Example file: first_fit.py

# explanations for member functions are provided in requirements.py

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = []

    for i, item in enumerate(items):
        placed = False
        for j, remaining in enumerate(bins):
            if item <= remaining:
                assignment[i] = j
                bins[j] = round(bins[j] - item, 2)
                placed = True
                break
        if not placed:
            assignment[i] = len(bins)
            bins.append(round(1.0 - item, 2))

    free_space[:] = bins



def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    # Step 1: Sort items in descending order with original indices
    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])

    bins = []  # Stores free space per bin

    for original_index, item in indexed_items:
        placed = False
        for j in range(len(bins)):
            if item <= bins[j]:
                assignment[original_index] = j
                bins[j] = round(bins[j] - item, 2)
                placed = True
                break

        if not placed:
            assignment[original_index] = len(bins)
            bins.append(round(1.0 - item, 2))

    # Final bin free space must be assigned *as is*
    free_space[:] = bins



