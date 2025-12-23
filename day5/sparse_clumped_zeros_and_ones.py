import bisect

class SparseClumpedZerosAndOnes():
    def __init__(self):
        self.clumps = []  # needs to remain sorted
    
    def any(self, start, end):
        if not self.clumps:
            return False

        idx1 = bisect.bisect_left(self.clumps, (start, start))
        idx2 = bisect.bisect_left(self.clumps, (end, end))
        found_some_between_start_and_end = idx1 < idx2
        
        if found_some_between_start_and_end:
            return True
        assert idx1 == idx2
        
        if idx1 == len(self.clumps):
            return self.clumps[idx1 - 1][1] >= start
        
        if idx1 == 0:
            return self.clumps[0][0] <= end
        
        if end >= self.clumps[idx1][0]:
            return True
        
        return self.clumps[idx1 - 1][1] >= start
        
    
    def set_ones(self, start, end):
        if self.any(start, end):
            # 1. Find the "Leftmost" range we touch
            # bisect_left gives insertion point. If we overlap the guy *before* that point,
            # we need to merge with him.
            idx1 = bisect.bisect_left(self.clumps, (start, start))
            if idx1 > 0 and self.clumps[idx1 - 1][1] >= start:
                idx1 -= 1  # We actually start merging from the previous clump

            # 2. Find the "Rightmost" range we touch
            # bisect_right is usually easier here to find the upper bound
            idx2 = bisect.bisect_right(self.clumps, (end, end))
            # If the clump at idx2 (the one after end) starts *at* end, bisect_right
            # pushes us past it. If the clump *before* idx2 ends after 'end', we merge it.
            if idx2 < len(self.clumps) and self.clumps[idx2][0] <= end:
                 idx2 += 1 # Include this one too (edge case for precise boundaries)

            # 3. Calculate the new Super-Range
            # The new start is min(my_input, start_of_first_touched_clump)
            new_start = min(start, self.clumps[idx1][0])
            
            # The new end is max(my_input, end_of_last_touched_clump)
            # Note: idx2 is the slice *stop* index, so we look at idx2-1
            new_end = max(end, self.clumps[idx2 - 1][1])

            # 4. Atomic Replace
            # Remove everything we touched and insert the one big merged result
            self.clumps[idx1:idx2] = [(new_start, new_end)]
            
        else:
            bisect.insort(self.clumps, (start, end))
        
        
        
    
    def __getitem__(self, index):
        if not self.clumps:
            return 0
        range_index_in_clumps = bisect.bisect_left(self.clumps, (index, index))
        if range_index_in_clumps == len(self.clumps):
            return int(index <= self.clumps[range_index_in_clumps - 1][1])
        elif self.clumps[range_index_in_clumps][0] == index:
            return 1
        elif range_index_in_clumps == 0:
            return 0
        elif self.clumps[range_index_in_clumps - 1][0] <= index <= self.clumps[range_index_in_clumps - 1][1]:
            return 1
        else:
           return 0
