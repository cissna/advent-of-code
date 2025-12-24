from collections import defaultdict
import heapq
import numpy as np


input_data = None
with open('data.txt') as f:
    input_data = f.read()
        
assert input_data


usable = input_data.strip()
arr = np.array([[int(x) for x in item.split(',')] for item in usable.split('\n')])

part1 = True
if part1:  # this solution is really inefficient but I wrote it right before I slept so it was fine to run for a while. fix with union find.
    best = set()
    graph = defaultdict(set)
    distances = []
    for item1 in arr:
        for item2 in arr:
            if tuple(item1) == tuple(item2):
                continue
            result = (np.linalg.norm(item1 - item2), frozenset((tuple(item1), tuple(item2))))
            if result in distances:
                continue
            heapq.heappush(distances, result)
    for i in range(1000):
        dist, (item1, item2) = heapq.heappop(distances)
        graph[item1].add(item2)
        graph[item1].add(item1)
        graph[item1] |= (graph[item2])
        for item in graph[item2]:
            graph[item] = graph[item1]
        graph[item2] = graph[item1]
        best = max(best, graph[item1], key=len)
    

    second = set()
    for key, value in graph.items():
        if key not in best:
            if len(value) > len(second):
                second = value
    third = set()
    for key, value in graph.items():
        if key not in best and key not in second:
            if len(value) > len(third):
                third = value
    print(len(best) * len(second) * len(third))
else:
    pass