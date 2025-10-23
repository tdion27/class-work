#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

#class player
class Player:
    def __init__(self, checker):
        """initializes the player object"""
        self.checker = checker 
        self.num_moves = 0
        
    def __repr__(self):
        """Returns a string that represets the player object"""
        s = 'Player ' 
        s += str(self.checker)
        return s 
    
    def opponent_checker(self):
        """Defines the opponent's checker"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """Get a next move for this player that is valid for the board b."""
        self.num_moves += 1 
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col 
            else:
                print('Try again!')
                
        
        
