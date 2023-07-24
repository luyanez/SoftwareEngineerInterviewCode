def square_sorted_array(nums):
    left = 0
    right = len(nums) - 1
    res = [0] * len(nums)
    n = len(nums) - 1

    while left <= right:
        print(nums[left])
        print(nums[right])
        if abs(nums[left]) > abs(nums[right]):
            res[n] = nums[left]**2
            left += 1
        else:
            res[n] = nums[right]**2
            right -=1
        n -= 1

        print("********")
    return res


nums = [-7,-3,2,3,11]
print(square_sorted_array(nums))