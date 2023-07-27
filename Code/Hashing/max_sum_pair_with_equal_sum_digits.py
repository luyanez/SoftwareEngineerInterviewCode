from collections import defaultdict

def sum_digits(num):
    dig_sum = 0
    while num:
        dig_sum += num % 10
        num //= 10
    return dig_sum

def maximum_sum_pair(nums):
    dic_num = defaultdict(int)
    ans = -1

    for num in nums:
        digit_num = sum_digits(num)
        if digit_num in dic_num:
            ans = max(ans, num + dic_num[digit_num])
        dic_num[digit_num] = max(dic_num[digit_num], num)

    return ans

nums = [18, 43, 36, 13, 7]
ans = maximum_sum_pair(nums)
print("The max sum of pairs with same sum of digits is: ", ans)