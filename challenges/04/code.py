import re

def read_file_horizontally(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()
    lines = [s.strip() for s in lines]
    return lines

def read_file_vertically(fp):
    rows = read_file_horizontally(fp)
    columns = []
    
    for i in range(len(rows[0])):
        column = ""
        for row in rows:
            column += row[i]
        columns.append(column)
    
    return columns

def read_file_diagonally(fp):
    """Reads a file diagonally, returning a list of diagonal strings."""
    lines = read_file_horizontally(fp)

    diagonals = []
    for i in range(len(lines)):
        diagonal = "" 
        row = i
        col = 0
        while row >= 0 and col < len(lines[row]):
            diagonal += lines[row][col] 
            row -= 1 
            col += 1 
        diagonals.append(diagonal) 

    for j in range(1, len(lines[0])): 
        diagonal = ""
        row = len(lines) - 1 
        col = j 
        while row >= 0 and col < len(lines[row]):
            diagonal += lines[row][col] 
            row -= 1 
            col += 1 
        diagonals.append(diagonal)

    return diagonals

def read_file_diagonally_rightward(fp):
    """Reads a file diagonally, returning a list of diagonal strings."""
    lines = read_file_horizontally(fp)

    diagonals = []
    for i in range(len(lines)): 
        diagonal = "" 
        row = i 
        col = len(lines) - 1 
        while row >= 0 and col < len(lines): 
            diagonal += lines[row][col]
            row -= 1 
            col -= 1 
        diagonals.append(diagonal) 

    for j in range(len(lines[0]), 1, -1): 
        diagonal = ""
        row = len(lines) - 1 
        col = j - 2 
        while row > 0 and col >= 0: 
            diagonal += lines[row][col] 
            row -= 1 
            col -= 1 
        diagonals.append(diagonal) 

    return diagonals

def count_xmas(s):
    matches = re.findall("XMAS", s)
    # print(f'{len(matches)} found in {s}')
    return len(matches)

n = 0

FILEPATH = 'challenges/04/data.txt'

rows = read_file_horizontally(FILEPATH)
for row in rows:
    n += count_xmas(row)
    n += count_xmas(row[::-1])

columns = read_file_vertically(FILEPATH)
for col in columns:
    n += count_xmas(col)
    n += count_xmas(col[::-1])

diagonals = read_file_diagonally(FILEPATH)
for diagonal in diagonals:
    n += count_xmas(diagonal)
    n += count_xmas(diagonal[::-1])

diagonals_r = read_file_diagonally_rightward(FILEPATH)
for diagonal_r in diagonals_r:
    n += count_xmas(diagonal_r)
    n += count_xmas(diagonal_r[::-1])

print(n)