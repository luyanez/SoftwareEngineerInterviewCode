from collections import defaultdict

def largestUniqueNumber(nums):
    tracker = defaultdict(int)

    for num in nums:
        tracker[num] += 1

    ans = -1
    for x in tracker:
        if tracker[x] == 1:
            ans = max(ans, x)

    return ans

nums = [5,7,3,9,4,9,8,1]
ans = largestUniqueNumber(nums)
print("Largest Unique Number is: ",ans)