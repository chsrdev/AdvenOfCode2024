with open("input.txt", 'r') as f:
    map = f.read().split('\n')
    x: int
    y: int
    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    curDir = 0
    for i in range(len(map)):
        if '^' in map[i]:
            x = map[i].index('^')
            y = i

    isInBounds = lambda x, y: 0 <= y < len(map) and 0 <= x < len(map[y])
    nextY = y + directions[curDir][1]
    nextX = x + directions[curDir][0]

    while isInBounds(nextX, nextY):
        nextY = y + directions[curDir][1]
        nextX = x + directions[curDir][0]

        while isInBounds(nextX, nextY) and map[nextY][nextX] != '#':
            map[nextY] = map[nextY][0:nextX] + '^' + map[nextY][nextX + 1:len(map[nextY])]
            map[y] = map[y][0:x] + 'X' + map[y][x + 1:len(map[y])]
            y = nextY
            x = nextX
            nextY = y + directions[curDir][1]
            nextX = x + directions[curDir][0]
        curDir = (curDir + 1) % 4

    map[y] = map[y][0:x] + 'X' + map[y][x + 1:len(map[y])]
    count = sum([i.count('X') for i in map])
    print(count)
