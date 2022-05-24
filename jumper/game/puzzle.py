from game.man import Man
import random

class Puzzle:
    """A word to be guessed. 
    
    The responsibility of Puzzle is provide a word from a words list to be guessed

    Attributes:
        word_list (List(str)): list of possible words to guess.
        word (str): randomly pick the word to guess from word_list.
        blank_puzzle(list): The initial state as well as the main list that will be updated for each guess
        _is_in_puzzle(boolean): every guess this will be update to return if the letter is in the word or not
        man(Man): The instance of a Man
    """

    def __init__(self):
        """Constructs a new Puzzle.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._word_list = ["mango", "house", "programming", "computer"]
        self._word = random.choice(self._word_list)
        self._blank_puzzle = ["_"] * len(self._word)
        self._is_in_puzzle = False
        self._man = Man() #add the man in the puzzle and remove it from the director
    
    def get_blank_puzzle(self):
        """Gets the puzzle hint(blank_puzzle).
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._blank_puzzle
          
    def get_word(self):
        """Gets the word.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        #self._word = random.choice(self._word_list) #add this in the initiation instead so tha we could call get_word without changing the word
        return self._word

    def check_guess(self, letter):
        """Check the guess of the player and update is_in_puzzle, blank_puzzle and man.fails when needed.
        
        Args:
            self (Puzzle): an instance of Puzzle.
            letter (str): input from user
        """
        self._is_in_puzzle = False
        for i in range(len(self._word)):
            if letter == self._word[i]:
                self._blank_puzzle[i] = letter
                self._is_in_puzzle = True
        if self._is_in_puzzle != True:
            self._man.fails += 1

    def is_winner(self):
        """Check if the underscores are no longer in the blank_puzzle, if true then the game is over.
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return "_" not in self._blank_puzzle