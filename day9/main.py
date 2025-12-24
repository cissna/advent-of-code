
input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data

usable = input_data.strip().split('\n')
part1 = False
if part1:
    m = 0
    for item1 in usable:
        for item2 in usable:
            # print(item1, item2)
            x1, y1 = [int(n) for n in item1.split(',')]
            x2, y2 = [int(n) for n in item2.split(',')]
            if (possible := (1+abs(y1 - y2)) * (1+abs(x1 - x2))) > m:
                m = possible
    print(m)
else:
    pass