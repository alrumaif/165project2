from decimal import Decimal, getcontext

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    assignment[:] = [-1] * len(items)
    free_space.clear()
    bins = []

    for i, item in enumerate(items):
        item_dec = Decimal(str(item))
        for j, space in enumerate(bins):
            if item_dec <= space:
                bins[j] -= item_dec
                assignment[i] = j
                break
        else:
            assignment[i] = len(bins)
            bins.append(Decimal('1.0') - item_dec)

    free_space[:] = [float(b.quantize(Decimal('0.01'))) for b in bins]


def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    free_space.clear()
    bins = []

    sorted_items = sorted(items, reverse=True)

    for i, item in enumerate(sorted_items):
        placed = False

        for j, space in enumerate(bins):
            if item <= space + 1e-8:
                bins[j] -= item
                assignment[i] = j  
                placed = True
                break
            
        if not placed:
            bins.append(1.0 - item)
            assignment[i] = len(bins) - 1

    free_space[:] = [round(b, 2) for b in bins]

