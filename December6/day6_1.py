with open("input.txt", 'r') as f:
    map = f.read().split('\n')

for i in range(len(map)):
    if '^' in map[i]:
        x = map[i].index('^')
        y = i
        break
else:
    exit()

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

curDir = 0
isInBounds = lambda x, y: 0 <= y < len(map) and 0 <= x < len(map[y])
visited = set()
nextY = y + directions[curDir][1]
nextX = x + directions[curDir][0]

while isInBounds(nextX, nextY):
    nextY = y + directions[curDir][1]
    nextX = x + directions[curDir][0]
    while isInBounds(nextX, nextY) and map[nextY][nextX] != '#':
        visited.add((x,y))
        y = nextY
        x = nextX
        nextY = y + directions[curDir][1]
        nextX = x + directions[curDir][0]
    curDir = (curDir + 1) % 4

visited.add((x,y))
print(len(visited))
