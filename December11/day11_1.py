import math
with open("input.txt", 'r') as f:
    stones = list(map(int, f.read().split()))
print(stones)
print(f'init: {stones}')
def change_stones(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif (int(math.log10(stones[i]))+1) % 2 == 0:
            num_len = int(math.log10(stones[i]))+1
            new_stones.append(int(stones[i]//(10**(num_len/2))))
            new_stones.append(int(stones[i]%(10**(num_len/2))))
        else:
            new_stones.append(stones[i]*2024)
    return new_stones

for i in range(25):
    stones = change_stones(stones)
    print(f'{i+1} blink: {len(stones)}')
