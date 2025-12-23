input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data


usable = input_data.strip()

fresh, available = usable.split('\n\n')

from sparse_clumped_zeros_and_ones import SparseClumpedZerosAndOnes  # noqa: E402
obj = SparseClumpedZerosAndOnes()

for line in fresh.split('\n'):
    start, end = line.split('-')
    start = int(start)
    end = int(end)

    obj.set_ones(start, end)

count_fresh = 0
for line in fresh.split('\n'):
    num = int(line)
    
    assert num

    count_fresh += obj[num]