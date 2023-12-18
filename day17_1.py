import heapq as hq
import math


f = open("day17_input.txt", "r")

grid = []

for i, line in enumerate(f.read().strip().split('\n')):
    grid.append(list(map(int, line)))

def dijkstra():
    visited = set()
    weights = {}
    path = {}
    queue = []
    weights[(0, 0, 'h')] = 0
    weights[(0, 0, 'v')] = 0
    hq.heappush(queue, (0, (0, 0, 'h')))
    hq.heappush(queue, (0, (0, 0, 'v')))
    while len(queue) > 0:
        (g, (i, j, dir)) = hq.heappop(queue)
        visited.add((i, j, dir))
        if dir == 'v':
            sum = 0
            for dist in range(1, 4):
                v = (i, j + dist, 'h')
                if j + dist < len(grid[0]):
                    sum += grid[i][j + dist]
                if j + dist < len(grid[0]) and v not in visited:
                    f = g + sum
                    if f < weights.get(v, math.inf):
                        weights[v] = f
                        path[v] = (i, j)
                        hq.heappush(queue, (f, v))
            sum = 0
            for dist in range(1, 4):
                v = (i, j - dist, 'h')
                if j - dist >= 0:
                    sum += grid[i][j - dist]
                if j - dist >= 0 and v not in visited:
                    f = g + sum
                    if f < weights.get(v, math.inf):
                        weights[v] = f
                        path[v] = (i, j)
                        hq.heappush(queue, (f, v))
        if dir == 'h':
            sum = 0
            for dist in range(1, 4):
                v = (i + dist, j, 'v')
                if i + dist < len(grid):
                    sum += grid[i + dist][j]
                if i + dist < len(grid) and v not in visited:
                    f = g + sum
                    if f < weights.get(v, math.inf):
                        weights[v] = f
                        path[v] = (i, j)
                        hq.heappush(queue, (f, v))
            sum = 0
            for dist in range(1, 4):
                v = (i - dist, j, 'v')
                if i - dist >= 0:
                    sum += grid[i - dist][j]
                if i - dist >= 0 and v not in visited:
                    f = g + sum
                    if f < weights.get(v, math.inf):
                        weights[v] = f
                        path[v] = (i, j)
                        hq.heappush(queue, (f, v))
    return weights

weights = dijkstra()

# print(weights)
print(min(weights[(len(grid)-1, len(grid[0])-1, 'v')], weights[(len(grid)-1, len(grid[0])-1, 'h')]))
