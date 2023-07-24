def way_to_split_array(nums):
    prefix = [nums[0]]

    for i in range(1,len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1
    return ans


nums = [10, 4, -8, 7]
ans = way_to_split_array(nums)
print("The number of ways to split the arr to get a left sum greater than or equal to the right section is: ", ans)


def waysToSplitArray(nums):
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans