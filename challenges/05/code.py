def read_file(FP):
    first_section = []
    second_section = []
    with open(FP, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if '|' in line:
            first_section.append(line.strip())
        elif ',' in line:
            second_section.append(line.strip())
        else:
            continue
    
    return first_section, second_section

def process_first_section(first_section):
    rv = {}
    for s in first_section:
        k = int(s.split('|')[0])
        v = int(s.split('|')[1])
        if k in rv.keys():
            rv[k].append(v)
        else:
            rv[k] = [v]
    return rv

def process_second_section(second_section):
    rv = []
    for s in second_section:
        l = [int(x) for x in s.split(',')]
        rv.append(l)
    return rv

def check_list_order(lst, val1, val2):
    ix1 = lst.index(val1)
    try:
        ix2 = lst.index(val2)
        if ix1 < ix2:
            return True
        else:
            return False
    except ValueError:
        return True

FP = 'challenges/05/data.txt'

first_section, second_section = read_file(FP)
clean_first_section = process_first_section(first_section)
clean_second_section = process_second_section(second_section)

n = 0

for lst in clean_second_section:
    for x in lst:
        # print(f'x: {x}')
        if x in clean_first_section.keys():
            # print(f'x is in clean_first_section keys')
            vals_to_check = clean_first_section[x]
            # print(f'Values to check comes after x: {vals_to_check}')
            for val in vals_to_check:
                # print(f'Checking value {val} comes after x')
                ordered = check_list_order(lst, x, val)
                # print(f'Value {val} comes after {x}: {ordered}')
                if not ordered:
                    break
            if not ordered:
                break
    if ordered:
        mid_val = lst[len(lst)//2]
        n += mid_val
    # print(f'{lst} is ordered: {ordered}')

print(n)