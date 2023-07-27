from collections import defaultdict

def minimum_consecutive_cards_pickup(cards):
    dic = defaultdict(int)
    ans = float("inf")
    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i - dic[cards[i]] + 1)
            
        dic[cards[i]] = i

    return ans if ans < float("inf") else -1

cards = [1,2,6,2,1]
ans = minimum_consecutive_cards_pickup(cards)
print("The lenght of the shortest subarray that contain at least one duplicate is: ",ans)
