with open("input.txt", 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0

    count = 0

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if lines[x][y] == 'A':
                r = lines[x-1][y-1] == 'M' and lines[x+1][y+1] == 'S'
                g = lines[x+1][y-1] == 'M' and lines[x-1][y+1] == 'S'
                b = lines[x+1][y-1] == 'S' and lines[x-1][y+1] == 'M'
                y = lines[x-1][y-1] == 'S' and lines[x+1][y+1] == 'M'
                if (r and (g or b)) or (y and (b or g)):
                    count += 1
print(count)

