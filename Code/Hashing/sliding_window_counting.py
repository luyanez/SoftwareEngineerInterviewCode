from collections import defaultdict

def sliding_window_counting(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range (len(s)):
        counts[s[right]] +=1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

s = "eceba"
k = 2
ans = sliding_window_counting(s,k)
print("The lenght of the longest substring that contains at most k distinct characters is: ", ans)