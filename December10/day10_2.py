with open("input.txt", 'r') as f:
    map = f.read().split('\n')

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

isInBounds = lambda x, y: 0 <= y < len(map) and 0 <= x < len(map[y])

def find_path(x, y):
    paths_count = 0
    for dir in directions:
        nextX = x + dir[0]
        nextY = y + dir[1]
        if isInBounds(nextX, nextY):
            if int(map[nextY][nextX]) == int(map[y][x]) + 1:
                if map[nextY][nextX] == '9':
                    paths_count += 1
                else:
                    paths_count += find_path(nextX, nextY)
    return paths_count

sum = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '0':
            sum += find_path(x, y)
print(sum)