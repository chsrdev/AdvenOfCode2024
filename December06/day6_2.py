with open("input.txt", 'r') as f:
    map = f.read().split('\n')

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

for j in range(len(map)):
    if '^' in map[j]:
        startX = map[j].index('^')
        startY = j
        break
else:
    exit()

isInBounds = lambda x, y: 0 <= y < len(map) and 0 <= x < len(map[y])
obstacles = [(startX, startY)]
count = 0

def patrol(map):
    global count
    curDir = 0
    x, y = startX, startY
    visited = set()
    rotatePoints = []
    nextY = y + directions[curDir][1]
    nextX = x + directions[curDir][0]

    while isInBounds(nextX, nextY):
        nextY = y + directions[curDir][1]
        nextX = x + directions[curDir][0]
        while isInBounds(nextX, nextY) and map[nextY][nextX] != '#':
            visited.add((x, y))
            y = nextY
            x = nextX
            nextY = y + directions[curDir][1]
            nextX = x + directions[curDir][0]
        curDir = (curDir + 1) % 4
        rotatePoints.append((x, y))
        if len(set(rotatePoints)) + 2 < len(rotatePoints):
            count += 1
            return 0
    visited.add((x, y))
    return visited


default_visited = patrol(map)
for j in default_visited:
    if j != (startX, startY):
        x, y = j
        mapCopy = map.copy()
        mapCopy[y] = mapCopy[y][0:x] + '#' + mapCopy[y][x + 1:len(mapCopy)]
        for j in range(len(obstacles) - 1):
            ox, oy = obstacles[j]
            mapCopy[oy] = mapCopy[oy][0:ox] + '.' + mapCopy[oy][ox + 1:len(mapCopy[oy])]
        patrol(mapCopy)

print(count)
