arr1 = []
arr2 = []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        l = list(map(int, line.split()))
        arr1.append(l[0])
        arr2.append(l[1])

arr1.sort()
arr2.sort()
similarity_score = 0

for i in range(0, len(arr1)):
    similarity_score += arr2.count(arr1[i]) * arr1[i]

print(similarity_score)
