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
            raise NotImplementedError("this shouldn't happen in the original use case, but if this were to be completed we would want to merge the ranges probably")
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
