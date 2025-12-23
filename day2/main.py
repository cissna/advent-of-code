input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data

usable = input_data.strip().split(',')

ranges = [range(int(item.split('-')[0]), int(item.split('-')[1])+1) for item in usable]

part1 = False
part2 = True
assert not part1 and part2

if part1:
    
    total = 0
    for rnge in ranges:
        for num in rnge:
            string = str(num)
            if len(string) % 2:
                continue  # it can't be a number repeated twice because it is odd in length (ignoring leading zeros)
            if string[:len(string)//2] == string[len(string)//2:]:
                total += num
    print(total)
elif part2:
    total = 0
    for rnge in ranges:
        for num in rnge:
            string = str(num)
            # find factors of the length of the string, as these are possible lengths of the repeating part
            factors = [i for i in range(1, min([int(len(string) ** 1/2) + 2, len(string)])) if not len(string) % i]
            for item in factors.copy():
                if item != 1:
                    complement = len(string) // item
                    if complement != item:
                        factors.append(len(string) // item)
            
            for factor in factors:
                first_such_substring = str(num)[:factor]  # e.g. string is 676767, factor=2, then this would be "676767"[0:2] -> "67"
                
                failed = False
                for i in range(factor, len(string), factor):  # e.g. range(2, 6, 2) -> (2, 4)
                    if str(num)[i:i+factor] != first_such_substring:
                        failed = True
                        break

                if not failed:
                    total += num
                    break
    print(total)
                        
                


    pass