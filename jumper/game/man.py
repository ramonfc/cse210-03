class Man:
    """A service that handles the man in parachute.
    
    The responsibility of a Man is to provide actions to deal with the man
    in parachutes
    """
    def __init__(self, word):
        self.fails = 0      
        self._word = word
        self._blank_puzzle = ["_"] * len(self._word)
        self._is_in_puzzle = False

    def get_blank_puzzle(self):
           return self._blank_puzzle
           

    def parachute(self):
        if self.fails < 1:
            victim =  """ 
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
             
            /___\ 
            \   /
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""
        elif self.fails < 3:
            victim =  """ 
             
             
            \   /
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""

        elif self.fails < 4:       
            victim =  """ 
             
             
          
             \ /
              o
             /|\ 
             / \ 

         ^^^^^^^^^^"""
        else:
            victim =  """ 
             
             
          
             
              x
             /|\ 
             / \ 

         ^^^^^^^^^^"""
            victim +="""\nYou died"""
        return victim

    def check_guess(self, letter):
        self._is_in_puzzle = False
        for i in range(len(self._word)):
            if letter == self._word[i]:
                self._blank_puzzle[i] = letter
                self._is_in_puzzle = True
        if self._is_in_puzzle != True:
            self.fails += 1

    def is_alive(self):
        return False if self.fails > 3 else True

    def is_winner(self):
        return "_" not in self._blank_puzzle