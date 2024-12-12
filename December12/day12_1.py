with open("input.txt", 'r') as f:
    map = f.read().split('\n')

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

is_in_bounds = lambda x, y: 0 <= y < len(map) and 0 <= x < len(map[y])

def get_perimeter_and_area(x, y, visited, this_region):
    if (x,y) in visited:
        return 0,0, this_region
    visited.add((x,y))
    region_type = map[y][x]
    perimeter = 0
    area = 1
    for dir in directions:
        nextX = x+dir[0]
        nextY = y+dir[1]
        if (is_in_bounds(nextX, nextY) and map[nextY][nextX] != region_type) or not is_in_bounds(nextX, nextY):
            perimeter += 1
        if is_in_bounds(nextX, nextY) and map[nextY][nextX] == region_type:
            this_region.add((nextX,nextY))
            res = get_perimeter_and_area(nextX, nextY, visited, this_region)
            perimeter += res[0]
            area += res[1]
    return perimeter, area, this_region

summ = 0
regions = set()
for y in range(len(map)):
    for x in range(len(map[y])):
        if (x,y) not in regions:
            res = get_perimeter_and_area(x, y, set(), {(x, y)})
            summ += res[0]*res[1]
            for i in res[2]:
                regions.add(i)
print(summ)
