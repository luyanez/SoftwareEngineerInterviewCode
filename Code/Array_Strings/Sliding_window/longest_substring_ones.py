def find_length(s):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

s = "11001011"
ans = find_length(s)
print("The lenght of the longest substring of 1's with only one 0 is: ",ans)