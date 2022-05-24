class Man:
    """A service that handles the man in parachute.
    
    The responsibility of a Man is to provide actions to deal with the man
    in parachutes
    """
    def __init__(self, word):
        self.fails = 0      
        self._word = word
        self._blank_puzzle = ["_"] * len(self._word) #creates the placeholders for the display for the letter 
        self._is_in_puzzle = False
        self._winning_word = '' 

    def get_blank_puzzle(self):
           return self._blank_puzzle
           

    def parachute(self):
        if self.fails < 1:
            victim =  """ 
            FINE
             ___
            /___\ 
            \   /
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""
        elif self.fails < 2:
            victim =  """ 
            WE HAVE A SMALL PROBLEM...
             
            /___\ 
            \   /
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""
        elif self.fails < 3:
            victim =  """ 
             UH OH...
             
            \   /
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""

        elif self.fails < 4:       
            victim =  """ 
             DANGER!!!
             
          
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""
        else:
            victim =  """ 
             G.A.M.E. O.V.E.R.
             
          
             
              x
             /|\ 
             / \ 

         ^^^^^^^^^^"""
            victim +="""\nYou died"""
        return victim

    def check_guess(self, letter): #this will update the fail count or change the "blank lines" to the correct letter if guessed
        self._is_in_puzzle = False
        for i in range(len(self._word)):
            if letter == self._word[i]:
                self._blank_puzzle[i] = letter
                
                self._winning_word += letter
                #print('this is winning word so far',self._winning_word) # debugging
                
                self._is_in_puzzle = True
        if self._is_in_puzzle != True:
            self.fails += 1  

    def is_alive(self):
        return False if self.fails > 3 else True

    def is_winner(self):
        return "_" not in self._blank_puzzle