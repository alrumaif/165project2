# Example file: best_fit.py

# explanations for member functions are provided in requirements.py

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
    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])
    bins = []

    for original_index, item in indexed_items:
        best_bin = -1
        min_leftover = float('inf')

        for j in range(len(bins)):
            if item <= bins[j]:
                leftover = bins[j] - item
                if leftover < min_leftover:
                    min_leftover = leftover
                    best_bin = j

        if best_bin != -1:
            assignment[original_index] = best_bin
            bins[best_bin] = round(bins[best_bin] - item, 2)
        else:
            assignment[original_index] = len(bins)
            bins.append(round(1.0 - item, 2))

    # Set free_space using bin index order
    bin_count = max(assignment) + 1
    free_space[:] = [0.0] * bin_count
    for i, space in enumerate(bins):
        free_space[i] = space

