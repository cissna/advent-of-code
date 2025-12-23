import numpy as np

input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data


usable = input_data


part1 = False
if part1:
    while '  ' in usable:
        usable = usable.replace('  ', ' ').strip()
    lines = [line.split() for line in usable.split('\n')]
    grid = np.array(lines)

    total = 0
    for row in grid.T:
        if row[-1] == '+':
            total += (sum([int(x) for x in row[:-1]]))
        else:
            assert row[-1] == '*'
            total += np.prod([int(x) for x in row[:-1]])
    print(total)
else:  # part 2:
    lines = [list(line) for line in usable.split('\n')]
    grid = np.array(lines)
    total = 0

    operator = None
    numbers = []
    for row in grid.T:
        row = list(row)
        if all(item == ' ' for item in row):
            # we move onto the next computation
            if operator == '+':
                total += sum(numbers)
            elif operator == '*':
                total += np.prod(numbers)
            del numbers[:]
        else:
            if row[-1] != ' ':
                operator = row[-1]
                row = row[:-1]
                assert(operator in ['+', '*'])
            numbers.append(int("".join(row)))
    if operator == '+':
        total += sum(numbers)
    elif operator == '*':
        total += np.prod(numbers)
    print(total)


