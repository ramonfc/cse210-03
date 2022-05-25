import re

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (str): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (str): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text, end = "\n"):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (str): The text to display.
            end (str): Specify what to print at the end.
        """
        print(text, end= end)


    def validateInput(self, message, expected_range):
        """Validate if the user input is an expected input

        Args: 
        self (Director): An instance of Director.
        message (str): message to ask to the user
        expected_range (str): regular expression corresponding to possible right options
        
        """
        user_input = input(message)
        user_input = user_input.lower()
        
        repeat = True
        while repeat == True:
            if re.match(expected_range, user_input) != None:
                if len(user_input) == 1:  
                   guess = user_input
                   repeat = False
                else:
                    print("Oh no! You entered more than one character. Please try again. Remember only one letter at a time.")
                    user_input = input(message)
                    repeat = True
            else:
                print("Bad input. You need to choose a letter between a - z. Please try again")
                user_input = input(message)
                repeat = True  
        return guess   
