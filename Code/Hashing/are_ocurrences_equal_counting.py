from collections import defaultdict
from collections import Counter

def are_ocurrences_equal(s):
    counts = defaultdict(int)

    for x in s:
        counts[x] += 1
    
    frequencies = counts.values()
    return len(set(frequencies)) == 1


## Bonus code using Collection's counter
def areOccurrencesEqual(self, s: str) -> bool:
    return len(set(Counter(s).values())) == 1


s = "aaabb"
ans = are_ocurrences_equal(s)
print("Check if all characters have equal number of ocurrences: ",ans)