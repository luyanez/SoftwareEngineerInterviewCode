def findMaxAverage(nums, k):
    curr = sum(nums[:k])

    ans = curr/k
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        temp_ans = curr/k
        ans = max(ans, temp_ans)

    return ans

nums = [1,12,-5,-6,50,3]
k = 4
ans = findMaxAverage(nums, k)
print("The maximum average subarray is : ",ans)