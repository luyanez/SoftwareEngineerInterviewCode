def fn(arr, target):
    left = 0
    curr = 0
    answer = 0

    for i in range(len(arr)):
        curr += arr[i]
    
        while curr > target:
            curr -= arr[left]
            left += 1

        answer = max(answer, i-left+1)
    
    return answer





arr = [1, 1, 1, 3]
t = 3
res = fn(arr, t)
print("The longest arr is: ",res)