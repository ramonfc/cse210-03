from game.puzzle import Puzzle
from game.man import Man
from game.terminal_service import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _puzzle (Puzzle): the word to guess.
        _is_playing (boolean): Whether or not to keep playing.
        _man (Man): The game's man in parachute.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
        _user_letter (str): the letter that the user input by console
    """
    def __init__(self):
        """The class constructor.
     
        Args:
        self (Director): an instance of Director.
        """
        self._is_playing = True
        self._puzzle = Puzzle().get_word()
        self._man = Man(self._puzzle)
        self._terminal_service = TerminalService()
        self._user_letter = ""
        
        
    def start_game(self):
        while self._is_playing:
            self.get_inputs()
            self.updates()
            self.get_outputs()
            
            
            
        
        
    def get_inputs(self):
        self._terminal_service.write_text("")
        for letter in self._man.get_blank_puzzle():
            self._terminal_service.write_text(letter, end= " ")

        self._terminal_service.write_text("")
        self._terminal_service.write_text(self._man.parachute()) #shows the parachute
        
        self._terminal_service.write_text("") #add newline that is blank
        self._user_letter= self._terminal_service.validateInput("Guess a letter [a-z]: ", "[a-z]") #gets user's letter 
        self._terminal_service.write_text(f"your input: {self._user_letter}") #displays the user's letter
        
        
        
    def updates(self):
        self._man.check_guess(self._user_letter)

       
        
    def get_outputs(self):
        print(self._man.parachute())
        continuing = self._man.fails #checks the fail count
        print(continuing,'this isthe fail count')
        if continuing == 4:
             self._is_playing = False
             print(self._is_playing,'this should say false')
             return self._is_playing
         
        else:
            
            if self._puzzle == self._man._winning_word:
                print('Congratulations YOU WIN!!!')
                self._is_playing = False
                return self._is_playing
            else:   
                
                self._is_playing = True
                print('this should be true', self._is_playing)
                return self._is_playing
        
    
    
    
    

    




# if __name__ == "__main__":   

#     d = Director()
#     # d.get_inputs()
#     # d.updates()
#     # d.get_outputs()
#     d.start_game()

