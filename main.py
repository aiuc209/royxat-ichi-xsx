def yigindisi(royxat):
    natija = []
    for ichki_roxyat in royxat:
        yigindi = sum(ichki_roxyat)
        natija.append(yigindi)
    return natija

royxat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(yigindisi(royxat))
