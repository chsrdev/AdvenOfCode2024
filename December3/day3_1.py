import re
with open("input.txt", 'r') as f:
    x = "".join(f.read().split('\n'))
    sum = 0
    sb = "mul\([0-9]+,[0-9]+\)"
    funcs = re.findall(sb, x)
    for i in funcs:
        z, y = map(int, re.findall('[0-9]+', i))
        sum += z*y
    print(sum)
