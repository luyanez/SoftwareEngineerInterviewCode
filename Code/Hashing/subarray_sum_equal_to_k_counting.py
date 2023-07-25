from collections import defaultdict

def subarray_sum(nums, k):
    counts = defaultdict(int)
    curr = ans = 0

    counts[0] = 1

    for num in nums:
        curr += num  #prefix sum
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


nums = [1, 2, 1, 2, 1]
k = 3
ans = subarray_sum(nums, k)
print("The number of subarrays whose sum is equal to k: ", ans)