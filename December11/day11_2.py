import math

with open("input.txt", 'r') as f:
    stones = list(map(int, f.read().split()))

def blink(stone, times, stones_size):
    if times == 0:
        return [1, stones_size]
    if (stone, times) in stones_size:
        return [stones_size[(stone, times)], stones_size]

    if stone == 0:
        size = blink(1, times - 1, stones_size)[0]
    elif (stone_len := (int(math.log10(stone) + 1))) % 2 == 0:
        left = stone // (10 ** (stone_len / 2))
        right = stone % (10 ** (stone_len / 2))
        size = blink(left, times - 1, stones_size)[0] + blink(right, times - 1, stones_size)[0]
    else:
        size = blink(stone * 2024, times - 1, stones_size)[0]
    stones_size[(stone, times)] = size
    return [size, stones_size]


size = 0
stones_size = {}
for stone in stones:
    blink_res = blink(stone, 75, stones_size)
    stones_size = blink_res[1]
    size += blink_res[0]
print(size)
