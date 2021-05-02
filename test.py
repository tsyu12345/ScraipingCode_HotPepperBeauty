def range_segmentation(maxindex):
    rang = list(range(2, maxindex, int(maxindex / 5)))
    print(rang)
    return rang

r = range_segmentation(2500)
