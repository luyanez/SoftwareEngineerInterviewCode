def two_sum(nums, target):
    dic = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]
        dic[num] = i

nums = [5, 2, 7, 10, 3, 9]
target = 8
ans = two_sum(nums, target)
print("The two indexes of the arr that sum equal to target are: ",ans)