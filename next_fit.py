# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bin_capacity = 1.0
    current_bin = 0
    remaining_capacity = bin_capacity

    for i, item in enumerate(items):
        if item <= remaining_capacity:
            # Place item in current bin
            assignment[i] = current_bin
            remaining_capacity -= item
        else:
            # Finalize current bin's free space
            free_space.append(round(remaining_capacity, 2))
            # Open a new bin
            current_bin += 1
            assignment[i] = current_bin
            remaining_capacity = bin_capacity - item

    # Finalize the last bin's free space
    free_space.append(round(remaining_capacity, 2))
