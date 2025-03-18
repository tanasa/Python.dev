from interactive_game import InteractiveGame
import random 

class Bagels(InteractiveGame):

    def __init__(self, num_digits = 3, max_attempts = 10):
        self.secret_number = self._generate_secret(num_digits)
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts

    def _generate_secret(self, num_digits):
        return ''.join(random.sample('123456789', num_digits))

    def get_instruction(self):
        return ("Instruction:\n"
                "Bagels: No digit is correct.\n"
                "Pico: One digit is correct but in the wrong position.\n"
                "Fermi: One digit is correct and in the correct position.\n")

    def get_status(self):
        return f"You have {self.remaining_attempts} chances to guess my secret."

    def can_continue(self):
        return self.remaining_attempts > 0

    def validate(self, guess):

        if not guess.isdigit() or len(guess) != 3:
            raise ValueError("Invalid guess. Enter a correct-length digit number.")

        if len(set(guess)) != 3:
            raise ValueError("Invalid guess. Digits must be unique.")
        
        if guess[0] == '0':
            raise ValueError("Invalid guess. Number cannot start with 0.")

        return guess

    def evaluate(self, guess):

        if guess == self.secret_number:
            return True, None
        
        result = []
        for i, digit in enumerate(guess):
            if digit == self.secret_number[i]:
                result.append("Fermi")
            elif digit in self.secret_number:
                result.append("Pico")
        
        if not result:
            result.append("Bagels")
        
        self.remaining_attempts -= 1
        return False, " ".join(result)

    def respond(self, result):
        
        if result:
            return "Congratulations! You guessed the number!"
        return f"Game Over! The secret number was: {self.secret_number}" 
