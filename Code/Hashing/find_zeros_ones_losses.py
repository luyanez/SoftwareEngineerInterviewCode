def findWinners(matches):
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        if winner not in one_loss or winner not in more_losses:
            zero_loss.add(winner)

        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)
        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)
        elif loser in more_losses:
            continue
        else:
            one_loss.add(loser)          
            
    return [sorted(list(zero_loss)), sorted(list(one_loss))]

        

matches = [[2,3],[1,3],[5,4],[6,4]]
ans = findWinners(matches)
print("The winners and losers are: ",ans)