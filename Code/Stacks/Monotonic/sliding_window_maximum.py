from collections import deque

def max_sliding_window(nums, k):
    ans = []
    queue = deque()

    for i in range(len(nums)):
        # maintain monotonic decreasing.
        # all elements in the deque smaller than the current one
        # have no chance of being the maximum, so get rid of them
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        if queue[0] + k == i:
            queue.popleft()

        if i >= k-1:
            ans.append(nums[queue[0]])
    return ans

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

ans = max_sliding_window(nums, k)
print("The max sliding window: ",ans)