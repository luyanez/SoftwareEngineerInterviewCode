from collections import Counter

def jewels_in_stones(jewels, stones):
    stones_count = Counter(stones)
    
    count = 0
    for s in stones_count:
        if s in jewels:
            count += stones_count[s]

    return count

def jewels_in_stones_set(jewels, stones):
    Jset = set(jewels)
    return sum(s in Jset for s in stones)

jewels = "aA"
stones = "aAAbbb"
ans = jewels_in_stones(jewels, stones)
print("The of jewels in stones are: ",ans)
ans2 = jewels_in_stones_set(jewels, stones)
print("Using a set: ", ans2)