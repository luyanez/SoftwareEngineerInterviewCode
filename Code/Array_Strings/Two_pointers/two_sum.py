def two_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return True
        elif curr > target:
            right -= 1
        else:
            left += 1
        
    return False




arr = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
res = two_sum(arr, target)
print("Target found: ",res)