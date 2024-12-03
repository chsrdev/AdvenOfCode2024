with open("input.txt", 'r') as f:
    x = "".join(f.read().split('\n'))
    is_enabled = True
    sum = 0
    for i in range(len(x)-8):
        if x[i:i+4] == 'do()':
            is_enabled = True
        elif x[i:i+7] == "don't()":
            is_enabled = False
        elif is_enabled and x[i:i+4] == 'mul(':
            z = i+4
            first_num = ""
            while x[z] in "0123456789":
                first_num += x[z]
                z+=1
            if x[z] == ',' and len(first_num) > 0:
                z += 1
                second_num = ""
                while x[z] in "0123456789":
                    second_num += x[z]
                    z += 1
                if x[z] == ')' and len(second_num) > 0:
                    sum += int(first_num) * int(second_num)
print(sum)