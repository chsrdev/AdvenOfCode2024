with open("input.txt", 'r') as f:
    antennas = f.read().split('\n')
isInBounds = lambda x, y: 0 <= y < len(antennas) and 0 <= x < len(antennas[y])
antipods = set()
for y1 in range(len(antennas)):
    for x1 in range(len(antennas[y1])):
        for y2 in range(y1, len(antennas)):
            for x2 in range(len(antennas[y2])):
                if x1 == x2 and y1 == y2: continue
                if antennas[y1][x1] == antennas[y2][x2] and antennas[y1][x1] != '.':
                    x_distance = x2-x1
                    y_distance = y2-y1
                    antipod_x = x1+(x_distance * 2)
                    antipod_y = y1+(y_distance * 2)

                    if isInBounds(antipod_x, antipod_y):
                        antipods.add((antipod_x, antipod_y))

                    antipod_x2 = x2-(x_distance * 2)
                    antipod_y2 = y2-(y_distance * 2)

                    if isInBounds(antipod_x2, antipod_y2):
                        antipods.add((antipod_x2, antipod_y2))
print(len(antipods))