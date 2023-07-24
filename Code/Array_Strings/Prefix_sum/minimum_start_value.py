def minimum_start_value(nums):
    startValue = 1
    while True:
        total = startValue
        isValid = True
        
        for num in nums:

            total += num
            if total < 1:
                isValid = False
                break

        if isValid:
            return startValue
        else:
            startValue += 1
        
        
nums = [1,-2,-3]
ans = minimum_start_value(nums)
print("The minimum start value is: ",ans)