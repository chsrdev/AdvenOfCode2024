def is_safe(arr: list) -> bool:
    is_increasing = True if arr[0]-arr[1] < 0 else False
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) > 3 or arr[i] - arr[i+1] == 0 or (arr[i] > arr[i+1] and is_increasing) or (arr[i] < arr[i+1] and not is_increasing):
            return False
    else:
        return True


with open("input.txt", 'r') as f:
    safe_count = 0
    for line in f.readlines():
        arr = list(map(int, line.split(" ")))
        if is_safe(arr):
            safe_count += 1

print(safe_count)
