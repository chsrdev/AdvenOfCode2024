with open("input.txt", 'r') as f:
    sum = 0
    for line in f.readlines():
        nums = list(map(int, "".join(line.split(":")).split(" ")))
        result = nums.pop(0)
        lastIter = [nums[0]]
        for i in range(1, len(nums)):
            thisIter = []
            for j in lastIter:
                thisIter.append(j + nums[i])
                thisIter.append(j * nums[i])
                thisIter.append(int(str(j)+str(nums[i])))
            lastIter = thisIter
        if result in lastIter:
            sum += result
    print(sum)
