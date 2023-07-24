def find_numbers(nums):
    seen_nums = set(nums)
    ans_nums = []
    for num in nums:
        if num-1 not in seen_nums and num+1 not in seen_nums:
            ans_nums.append(num)

    return ans_nums

nums = [5, 2, 7, 10, 3, 9]
ans = find_numbers(nums)
print("The final arr with the nums that are valid for the condition x+1 not in nums and x-1 not in nums are: ", ans)