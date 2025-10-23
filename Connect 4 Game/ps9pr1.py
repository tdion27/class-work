#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        self.height = height
        self.width = width 
        self.slots = [[' '] * width for r in range(height)]
    


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for i in range(self.width * 2 + 1):
            s += '-' 
        s += '\n'
        for x in range(self.width):
            index = x % 10
            s += ' ' + str(index)
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        for r in range(len(self.slots) - 1):
            if self.slots[row + 1][col] != ' ':
                break
            elif self.slots[row][col] == ' ':
                row += 1
        self.slots[row][col] = checker
        

  
    ### add your reset method here ###
    def reset(self):
        """resets the board"""
        self.slots = [[' '] * self.width for r in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """determines if a checker can be added to a column"""
        if col > (len(self.slots[0]) - 1) or col < 0:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True 
    
    def is_full(self):
        """determines if a board object is full of checkers"""
        for r in range(len(self.slots)):
            for c in range(len(self.slots[0])):
                if self.slots[r][c] == ' ':
                    return False
        return True

    def remove_checker(self, col):
        """removes the top checker in col of a board object"""
        top_checker = 0
        for r in range(len(self.slots) - 1):
            if self.slots[top_checker][col] != ' ':
                break
            elif self.slots[top_checker][col] == ' ':
                top_checker += 1
        self.slots[top_checker][col] = ' '
        
    # Win Checkers:
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker."""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """Checks for a diagonal win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """Checks for a diagonal win for the specified checker"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ Checks for all wins for the specified checker"""
        assert(checker == 'X' or checker == 'O')
    
        if self.is_horizontal_win(checker) == True:
            return True 
        if self.is_vertical_win(checker) == True:
            return True 
        if self.is_up_diagonal_win(checker) == True:
            return True 
        if self.is_down_diagonal_win(checker) == True:
            return True 
        return False 
                                    
        
            