def count_elements(arr):
    uni_nums = set(arr)
    count = 0
    for x in uni_nums:
        if x+1 in uni_nums:
            count += 1

    return count

nums = [1,1,2,2]
ans = count_elements(nums)
print("Total of elements x, such as x+1 is also in the array: ",ans)