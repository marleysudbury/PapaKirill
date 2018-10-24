def calc_score(s, e):
    player_score_steps = int((1/s)*100000)
    player_score_ev = len(e) * 800
    # if len(evidence) == :
    # player_score_ev = player_score_ev + 5000
    player_score = player_score_steps + player_score_ev
    return player_score


print("Score: ", calc_score())
