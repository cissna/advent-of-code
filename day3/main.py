input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data

usable = input_data.strip().split('\n')
# parts 1/2:
N = 12
total = 0
for row in usable:
    result = ""
    first_valid_digit = 0    
    for i in range(N-1, -1, -1):
        substring = row[first_valid_digit:len(row)-i]
        pick = first_valid_digit + max(range(len(substring)), key=lambda x: substring[x])
        result += row[pick]

        first_valid_digit = pick + 1

    total += int(result)

print(total)

