import re
import numpy as np

with open('challenges/03/data.txt', 'r') as f:
    text = f.read()

pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, text)

n = 0

for match in matches:
    numbers = [int(x) for x in re.findall(r"\d+", match)]
    product = np.prod(numbers)
    n += product

print(n)

pattern_to_exclude = r"don't\(\)(.*?)do\(\)"
new_text = re.sub(pattern_to_exclude, '', text, flags=re.DOTALL)

with open('challenges/03/new_text.txt', 'w') as f:
    f.write(new_text)

matches = re.findall(pattern, new_text)

n = 0

for match in matches:
    numbers = [int(x) for x in re.findall(r"\d+", match)]
    product = np.prod(numbers)
    n += product

print(n)