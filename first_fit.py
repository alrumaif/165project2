
# Example file: first_fit.py

# explanations for member functions are provided in requirements.py

from decimal import Decimal, getcontext
from zipzip_tree import ZipZipTree

from decimal import Decimal

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    for i in range(len(items)):
        assignment[i] = -1
    free_space.clear()

    bins = []  # list of Decimal remaining capacities

    for i, item in enumerate(items):
        item_dec = Decimal(str(item))
        placed = False

        for j in range(len(bins)):
            if item_dec <= bins[j]:
                assignment[i] = j
                bins[j] -= item_dec
                placed = True
                break

        if not placed:
            assignment[i] = len(bins)
            bins.append(Decimal('1.0') - item_dec)

    free_space[:] = [float(b.quantize(Decimal('0.01'))) for b in bins]



def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    indexed_items = sorted(enumerate(items), key=lambda x: -x[1])

    bins = [] 
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

    free_space[:] = [round(cap, 2) for cap in bins]
