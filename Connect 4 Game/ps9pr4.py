#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """Creates a new AI Player"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak 
        self.lookahead = lookahead
    
    def __repr__(self):
        """Returns a string that represents the AI Player"""
        s = 'Player ' 
        s += str(self.checker)
        s += ' (' 
        s += str(self.tiebreak) + ', ' + str(self.lookahead)
        s += ')'
        return s 
    
    def max_score_column(self, scores):
        """Choses the maximum score from a list and returns the index, 
        taking into account ties and using the players tiebreaking strategy"""
        indices = []
        max_score = max(scores)
        for i in range(len(scores)):
            if scores[i] >= max_score:
                indices += [i]
        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        else:
            return random.choice(indices)
        
    def scores_for(self, b):
        """Determines the AI player's scores for each column on the board"""
        scores = [50] * b.width 
        for i in range(len(scores)):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0 
            elif self.lookahead == 0:
                scores[i] = 50 
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                if 100 in opp_scores:
                    scores[i] = 0
                elif 0 in opp_scores:
                    scores[i] = 100
                b.remove_checker(i)
        return scores
    
    def next_move(self, b):
        """Makes the AI Player's next move"""
        scores = self.scores_for(b)
        index = self.max_score_column(scores)
        self.num_moves += 1 
        return index
        
        
        