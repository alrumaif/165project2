
# Example file: first_fit.py

# explanations for member functions are provided in requirements.py

from decimal import Decimal, getcontext
from zipzip_tree import ZipZipTree
from decimal import Decimal

def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    for i in range(len(items)):
        assignment[i] = -1
    free_space.clear()

    bins = [] 

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

