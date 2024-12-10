with open("input.txt", 'r') as f:
    rulesStr, updatesStr = f.read().split("\n\n")
    rules = []
    updates = []

    for rule in rulesStr.split('\n'):
        rules.append(list(map(int, rule.split('|'))))
    for update in updatesStr.split('\n'):
        updates.append(list(map(int, update.split(','))))

    sum = 0
    for update in updates:
        isOkUpdate = True
        for rule in rules:
            if rule[0] in update and rule[1] in update and update.index(rule[0]) >= update.index(rule[1]):
                    isOkUpdate = False
        if isOkUpdate:
            sum += update[len(update)//2]
    print(sum)