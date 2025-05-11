
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    bins = []

    for i, item in enumerate(items):
        best_bin = -1
        min_leftover = float('inf')

        for j, space in enumerate(bins):
            if item <= space:
                leftover = space - item
                if leftover < min_leftover:
                    min_leftover = leftover
                    best_bin = j

        if best_bin != -1:
            bins[best_bin] = round(bins[best_bin] - item, 2)
            assignment[i] = best_bin
        else:
            bins.append(round(1.0 - item, 2))
            assignment[i] = len(bins) - 1

    free_space[:] = bins


def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.clear()
    bins = []

    sorted_items = sorted(items, reverse=True)

    for i, item in enumerate(sorted_items):
        best_bin = -1
        min_leftover = float('inf')

        for j, space in enumerate(bins):
            if item <= space + 1e-8:
                leftover = space - item
                if leftover < min_leftover:
                    min_leftover = leftover
                    best_bin = j

        if best_bin != -1:
            bins[best_bin] -= item
            assignment[i] = best_bin
        else:
            bins.append(1.0 - item)
            assignment[i] = len(bins) - 1

    free_space[:] = [round(b, 2) for b in bins]
