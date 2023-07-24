def running_sum(nums):
    ans = [nums[0]]
    for i in range(1, len(nums)):
        ans.append(nums[i] + ans[-1])
    return ans

nums = [1,2,3,4]
ans = running_sum(nums)
print("The array running sum is: ",ans)