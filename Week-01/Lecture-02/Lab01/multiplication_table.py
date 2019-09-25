n = int(input('N: '))

rows = []

for r in range(1, n + 1):
    for c in range(r):
        if r == 1:
            rows.append([r])
        if r == 2:
            rows.append([r*(r-1), (r*r)])
            break
        if r == 3:
            rows.append([r*(r-2), r*(r-1), (r*r)])
            break

print(rows)