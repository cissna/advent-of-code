import numpy as np

input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data


usable = input_data.strip().split('\n')


def string_to_numpy(data_strings):
    # Split the string by newlines and convert each character 
    # into an integer (1 if '@', else 0)
    grid = [
        [1 if char == '@' else 0 for char in line] 
        for line in data_strings
    ]
    
    return np.array(grid)

def sum_neighbors(arr):
    # The result array will be (height-2, width-2)
    # We slice the original array to get the 8 neighbors
    
    # Neighbors:
    top_left  = 1 - arr[0:-2, 0:-2]
    top_mid   = 1 - arr[0:-2, 1:-1]
    top_right = 1 - arr[0:-2, 2:]
    
    mid_left  = 1 - arr[1:-1, 0:-2]
    mid_mid = arr[1:-1, 1:-1] # <-- ignore center from sum
    mid_right = 1 - arr[1:-1, 2:]
    
    bot_left  = 1 - arr[2:,   0:-2]
    bot_mid   = 1 - arr[2:,   1:-1]
    bot_right = 1 - arr[2:,   2:]
    
    # Sum them all up
    neighbor_sum = (top_left + top_mid + top_right +
                    mid_left +           mid_right +
                    bot_left + bot_mid + bot_right)
    
    return neighbor_sum * mid_mid  # mid_mid is 0 or 1 so it will 0 out unless we are at a roll.

arr = string_to_numpy(usable)


def process_once(arr):
    # pad with zeros to simplify computations (you can also use `np.pad(arr, ((1, 1), (1, 1)), mode='constant', constant_values=0)` but that's cheating from AI)
    row_zeros = np.zeros(arr.shape[1])

    arr = np.vstack([row_zeros, arr])
    arr = np.vstack([arr, row_zeros])

    col_zeros = np.zeros(arr.shape[0])
    col_zeros_2d = col_zeros[:, None]

    arr = np.hstack([col_zeros_2d, arr])
    arr = np.hstack([arr, col_zeros_2d])



    processed = sum_neighbors(arr) > 4
    return processed

total = -1
update_amount = 1  # so the while loop starts but we effectively initialize this to 0
while update_amount:
    total += update_amount
    processed = process_once(arr)
    update_amount = processed.sum()

    arr -= processed

print(total)