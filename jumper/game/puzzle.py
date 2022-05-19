import random
class Puzzle:
    """A word to be guessed. 
    
    The responsibility of Puzzle is provide a word from a words list to be guessed

    Attributes:
        word_list (List(str)): list of possible words to guess.
        word (str): the word to guess.
        
    """

    def __init__(self):
        self._word_list = ["mango", "house", "programming", "computer"]
        self._word = ""

    def get_word(self):
       self._word = random.choice(self._word_list)
       return self._word
