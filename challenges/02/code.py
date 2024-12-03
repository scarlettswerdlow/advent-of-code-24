import pandas as pd

with open('challenges/02/data.txt', 'r') as f:
    rows = [list(map(int, line.split())) for line in f]

n = 0

for row in rows:
    s = pd.Series(row)
    diff = s.diff()
    monotonic = ((diff[1:] > 0).all()) | ((diff[1:] < 0).all())
    gradual = ((diff[1:].abs().between(1, 3, inclusive='both'))).all()
    safe = monotonic * gradual
    if safe:
        n += 1

print(n)