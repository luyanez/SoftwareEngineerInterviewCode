from collections import defaultdict

def group_anagrams(anagrams):
    groups = defaultdict(list)

    for value in anagrams:
        key = "".join(sorted(value))
        groups[key].append(value)

    return groups.values()

strs = ["eat","tea","tan","ate","nat","bat"]
ans = group_anagrams(strs)
print("The group of anagrams are: ",ans)