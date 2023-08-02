from collections import defaultdict
def longest_substring(s):
    sdic = defaultdict(int)
    ans = j = 0

    for i in range(len(s)):
        if s[i] in sdic:
            j = max(sdic[s[i]], j)
        
        ans = max(ans, i-j+1)  #right - left + 1
        sdic[s[i]] = i+1

    return ans

s = "abcabcbb"
ans = longest_substring(s)
print("The length of the longest substring without repeated characters is: ",ans)

        