def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    ans = []

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])


    for x,y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)
    
    return ans

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
ans = answer_queries(nums, queries, limit)
print("Boolean array, ",ans)