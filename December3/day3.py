import re
with open("input.txt", 'r') as f:
    x = "".join(f.read().split('\n'))
    is_enabled = True
    sum = 0
    sb = "(don't\(\)|do\(\)|mul\([0-9]+,[0-9]+\))"
    funcs = re.findall(sb, x)
    for i in funcs:
        if i == 'do()':
            is_enabled = True
        elif i == "don't()":
            is_enabled = False
        elif is_enabled:
            z, y = map(int, re.findall('[0-9]+', i))
            sum += z*y
    print(sum)
