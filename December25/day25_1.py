with open("input.txt") as file:
    objects = file.read().split('\n\n')
    locks = list()
    keys = list()

    for el in objects:
        lines = el.split()
        heights = []
        for j in range(5):
                count = 0
                for i in range(1, 6):
                    count += 1 if lines[i][j] == '#' else 0
                heights.append(count)
        if '.' in lines[0]:
             keys.append(heights)
        else:        
             locks.append(heights)
    
    checked = list(())
    count = 0
    for lock in locks:
        heights = []
        for h in lock:
            heights.append(5 - h)
        for key in keys:
            if (lock, key) in checked:
                 continue
            checked.append((lock, key))
            is_ok = True
            for i in range(5):
                if key[i] > heights[i]:
                     is_ok = False
            if is_ok:
                 count += 1
    print(count)