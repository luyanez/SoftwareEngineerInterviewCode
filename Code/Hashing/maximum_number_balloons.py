
def maximum_number_balloons(text):
    balloon_text = {'b':0,'a':0,'l':0,'o':0,'n':0}
    ans = 0

    for w in text:
        if w in balloon_text:
            balloon_text[w] +=1

    balloon_text['l'] //= 2
    balloon_text['o'] //= 2

    if balloon_text['b'] >= 1 and balloon_text['a'] >= 1 and balloon_text['l'] >= 1 and balloon_text['o'] >= 1 and balloon_text['n'] >= 1:
        ans = min(balloon_text.values())
    
    return ans

text = "balllllllllllloooooooooon"
ans = maximum_number_balloons(text)
print("Number of balloons in text is: ",ans)
