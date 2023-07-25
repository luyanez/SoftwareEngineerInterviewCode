from collections import defaultdict

def number_of_nice_subarrays(nums, k):
    counts = defaultdict(int)
    curr = ans = 0

    counts[0] = 1

    for num in nums:
        curr += num % 2  #prefix sum
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


nums = [1, 1, 2, 1, 1]
k = 3
ans = number_of_nice_subarrays(nums, k)
print("The number of nice subarrays with exactly k odd numbers is: ", ans)