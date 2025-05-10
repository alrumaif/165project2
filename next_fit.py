# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bin_capacity = 1.0
    current_bin = 0
    remaining_capacity = bin_capacity
    temp_free_space = []

    for i, item in enumerate(items):
        if item <= remaining_capacity:
            assignment[i] = current_bin
            remaining_capacity -= item
        else:
            temp_free_space.append(round(remaining_capacity, 2))
            current_bin += 1
            assignment[i] = current_bin
            remaining_capacity = bin_capacity - item

    temp_free_space.append(round(remaining_capacity, 2))
    free_space[:] = temp_free_space

