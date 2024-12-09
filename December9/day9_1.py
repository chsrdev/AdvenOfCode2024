with open("input.txt", 'r') as f:
    disk = f.read()

disk_list = []
id = 0
for i in range(len(disk)):
    if i % 2 == 0:
        disk_list.extend([id] * int(disk[i]))
        id += 1
    else:
        disk_list.extend(['.'] * int(disk[i]))

l, r = 0, len(disk_list) - 1

while l < r:
    if disk_list[l] == '.':
        disk_list[l], disk_list[r] = disk_list[r], '.'
        r -= 1
    else:
        l += 1

checksum = 0
idx = 0

for i in range(len(disk_list)):
    if disk_list[i] != '.':
        checksum += disk_list[i] * idx
        idx += 1

# print(disk_list)
print("Checksum:", checksum)
