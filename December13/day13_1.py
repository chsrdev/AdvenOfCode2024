with open("input.txt", 'r') as f:
    claw_machines = f.read().split('\n\n')
    summ = 0
    for machine in claw_machines:
        m = machine.split("\n")
        a_button = "".join(m[0].split(',')).split('+')
        b_button = "".join(m[1].split(',')).split('+')
        prize = "".join(m[2].split(',')).split('=')
        a_x, a_y = int(a_button[1].split(' ')[0]), int(a_button[2])
        b_x, b_y = int(b_button[1].split(' ')[0]), int(b_button[2])
        prize_x, prize_y = int(prize[1].split(' ')[0]), int(prize[2])

        found = False
        for a_idx in range(100):
            for b_idx in range(100):
                x = a_idx * a_x + b_idx * b_x
                y = a_idx * a_y + b_idx * b_y
                if x == prize_x and y == prize_y:
                    summ += a_idx * 3 + b_idx
                    found = True
                    break
            if found: break
    print(summ)
