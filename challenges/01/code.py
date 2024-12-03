import pandas as pd

df = pd.read_csv('challenges/01/data.txt', sep = '   ', engine = 'python', header = None, dtype = int)
df_sorted = pd.concat([pd.Series(df[col].sort_values().to_list()) for col in df.columns], axis = 1)

# print(abs(df_sorted[0] - df_sorted[1]).sum())

df_left = df[0]
df_right = df[1]

similiarity_score = 0
for item in df_left:
    n = len(df_right[df_right == item])
    similiarity_score += item*n

print(similiarity_score)