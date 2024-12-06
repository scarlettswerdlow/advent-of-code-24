import pandas as pd

with open('challenges/02/data.txt', 'r') as f:
    rows = [list(map(int, line.split())) for line in f]

def is_safe(diff):
    monotonic = ((diff[1:] > 0).all()) | ((diff[1:] < 0).all())
    gradual = ((diff[1:].abs().between(1, 3, inclusive='both'))).all()
    safe = monotonic * gradual
    return safe

n = 0

for row in rows:
    s = pd.Series(row)
    diff = s.diff()
    safe = is_safe(diff)
    if safe:
        n += 1

print(f'Safe reports: {n}')

n = 0

for row in rows:
    s = pd.Series(row)
    diff = s.diff()
    safe = is_safe(diff)
    if safe:
        n += 1
    else:
        for i in range(len(s)):
            s_pd = s.drop(i)
            diff_pd = s_pd.diff()
            safe_pd = is_safe(diff_pd)
            if safe_pd:
                n += 1
                break

print(f'Safe reports with Problem Dampener: {n}')