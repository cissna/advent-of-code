input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data


usable = input_data.strip()
part1 = False
if part1:
    indices = set()
    splits = 0

    for row in usable.split('\n'):
        try:
            indices.add(row.index('S'))
        except ValueError:
            to_add = set()
            to_subtract = set()
            for index in indices:
                if row[index] == '^':
                    splits += 1
                    assert index and index + 1 != len(row)

                    to_add.add(index - 1)
                    to_add.add(index + 1)
                    to_subtract.add(index)
            assert not (to_subtract.intersection(to_add))
            indices.update(to_add)
            indices.difference_update(to_subtract)
            
    print(splits)
else:
    from collections import defaultdict
    indices = defaultdict(int)
    splits = 1

    for row in usable.split('\n'):
        try:
            indices[row.index('S')] += 1
        except ValueError:
            changes = defaultdict(int)
            for index in indices:
                if row[index] == '^' and indices[index]:
                    splits += indices[index]
                    assert index and index + 1 != len(row)

                    changes[index - 1] += indices[index]
                    changes[index + 1] += indices[index]
                    changes[index] -= indices[index]
            for change in changes:
                indices[change] += changes[change]
    print(splits)
            