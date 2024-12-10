with open("input.txt", 'r') as f:
    disk = f.read()

disk_list = []
id = 0
for i in range(len(disk)):
    if i % 2 == 0:
        disk_list.extend([[id] * int(disk[i])])
        id += 1
    else:
        if int(disk[i]) > 0:
            disk_list.extend([['.'] * int(disk[i])])

r = len(disk_list) - 1

while r > 0:
    _l = 0
    while _l < r:
        if disk_list[r][0] == '.':
            r -= 1
            break
        if disk_list[_l][0] == '.' and len(disk_list[_l]) >= len(disk_list[r]):
            len_l = len(disk_list[_l]) - len(disk_list[r])
            disk_list[_l], disk_list[r] = disk_list[r], ['.'] * len(disk_list[r])
            if len_l > 0:
                disk_list.insert(_l+1, ['.'] * len_l)
                r += 1
            r -= 1
            break
        else:
            _l += 1
    else: r-=1

disk_list_s = []
for i in disk_list:
    for x in i:
        disk_list_s.append(x)
checksum = 0
idx = 0

for i in range(len(disk_list_s)):
    if disk_list_s[i] != '.':
        checksum += disk_list_s[i] * idx
    idx += 1

print("Checksum:", checksum)
