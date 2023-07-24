def missing_number(nums):
    numset = set(nums)
    n = len(nums) + 1
    for i in range(n):
        if i not in numset:
            return i

def missing_numbers_gauss(nums):
    gaus_nums = len(nums) * (len(nums) + 1) // 2
    ord_sum = sum(nums)
    return gaus_nums - ord_sum
        
nums = [9,6,4,2,3,5,7,0,1]
ans = missing_number(nums)
print("The missing number is: ",ans)

ans_gaus = missing_numbers_gauss(nums)
print("The missing number is: ",ans_gaus)

