from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)

    for arr in nums:
        for val in arr:
            counts[val] += 1

    n = len(nums)
    ans = []
    print(counts)

    for key in counts:
        if counts[key] == n:
            ans.append(key)

    return sorted(ans)

nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
ans = intersection(nums)
print("The only values that appear in all the arrays are: ",ans)