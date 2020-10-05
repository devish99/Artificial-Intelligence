# Creating a class for the game to be played
class TicTacToe:
    def __init__(self):
        self.initialize_game()

    # Creating the empty board
    def initialize_game(self):
        self.current_state = [['_','_','_'],
                              ['_','_','_'],
                              ['_','_','_']]

        # Player X always plays first
        self.player_turn = 'X'

    # Drawing the empty board
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{} |'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Determines if the move made is valid
    def is_valid(self, px, py):
        
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '_':
            return False
        else:
            return True

    # Checks if the game has ended and returns the winner in each case
    def is_end(self):

        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '_' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # First diagonal win
        if (self.current_state[0][0] != '_' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '_' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is the board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # If there is an empty field, we continue the game
                if (self.current_state[i][j] == '_'):
                    return None

        # It's a tie!
        return '_'

    # Player 'O' is the maximizer, in this case the computer
    def max(self):
        '''
         Possible values for maxv are:
         -1 - loss
         0  - a tie
         1  - win
         We're initially setting it to -2 as worse than the worst case:
        '''
        maxv = -2

        px = None
        py = None

        result = self.is_end()
        '''
         If the game came to an end, the function needs to return
         the evaluation function of the end. That can be:
         -1 - loss
         0  - a tie
         1  - win
        '''
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    '''
                     On the empty field, player 'O' makes a move and calls Min
                     That's one branch of the game tree.
                    '''
                    self.current_state[i][j] = 'O'

                    # m is used to decide if the human has the upper hand or not
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j

                    # Setting back the field to empty
                    self.current_state[i][j] = '_'
        return (maxv, px, py)

    # Player 'X' is the minimizer, in this case the human
    def min(self):
        '''
         Possible values for minv are:
         -1 - win
         0  - a tie
         1  - loss
         We're initially setting it to 2 as worse than the worst case:
        '''
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    self.current_state[i][j] = 'X'

                    # m is used to decide if the computer has the upper hand or not
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '_'

        return (minv, qx, qy)

    def play(self):

        # Initializing the coordinates of each space in the board as a dictionary
        board_coordinates={'1':(0,0),'2':(0,1),'3':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'7':(2,0),'8':(2,1),'9':(2,2)}
        
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '_':
                    print("It's a tie!")

                self.initialize_game()
                return

            # If it is the human's turn
            if self.player_turn == 'X':

                while True:

                    (m, qx, qy) = self.min()
                    
                    num = str(input("Enter the number of field (1 to 9): "))
                    
                    get_num = num
                    (px,py) = board_coordinates[get_num]

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid move! Try again.')

            # If it is the computer's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

# Main function to excecute the above functions and begin the game
def main():
    g = TicTacToe()
    g.play()

# Driver Code
if __name__ == "__main__":
    main()