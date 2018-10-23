from player import player_steps
from player import evidence
def calc_score():
    global player_steps
    global evidence
    player_score_steps = int((1/player_steps)*100000)
    player_score_ev = len(evidence) * 800
    #if len(evidence) == :
        #player_score_ev = player_score_ev + 5000   
    player_score = player_score_steps + player_score_ev
    return player_score

print("Score:",calc_score())
