from puzzle import Puzzle
from man import Man
from terminal_service import TerminalService

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

    def get_inputs(self):
        self._terminal_service.write_text("")
        for letter in self._man.get_blank_puzzle():
            self._terminal_service.write_text(letter, end= " ")

        self._terminal_service.write_text("")
        self._terminal_service.write_text(self._man.parachute())
        
        self._terminal_service.write_text("")
        self._user_letter= self._terminal_service.validateInput("Guess a letter [a-z]: ", "[a-z]")
        self._terminal_service.write_text(f"your input: {self._user_letter}")

    




if __name__ == "__main__":   

    d = Director()
    d.get_inputs()

