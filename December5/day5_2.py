def isOkUpdate(update: list, rules: list) -> bool:
    isOkUpdate = True
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[0]) >= update.index(rule[1]):
            isOkUpdate = False
    return isOkUpdate


def swap(l: list, x: int, y: int) -> list:
    temp = l[x]
    l[x] = l[y]
    l[y] = temp
    return l


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
        if not isOkUpdate(update, rules):
            while not isOkUpdate(update, rules):
                for rule in rules:
                    if rule[0] in update and rule[1] in update and update.index(rule[0]) >= update.index(rule[1]):
                        swap(update, update.index(rule[0]),
                             update.index(rule[1]))
            sum += update[len(update)//2]
    print(sum)
