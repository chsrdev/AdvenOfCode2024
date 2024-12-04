with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    target = "XMAS"
    count = 0

    def check_word(x, y, dx, dy):
        for k in range(len(target)):
            nx, ny = x + k * dx, y + k * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or lines[nx][ny] != target[k]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    count += 1

print(count)
