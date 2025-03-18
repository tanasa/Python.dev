from abc import ABC, abstractmethod

class InteractiveGame(ABC):
    @abstractmethod
    def get_instruction(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    def _get_prompt(self):
        return 'What is your guess? '

    @abstractmethod
    def can_continue(self):
        pass

    @abstractmethod
    def validate(self, guess):
        pass

    @abstractmethod
    def evaluate(self, valid_guess):
        pass

    @abstractmethod
    def respond(self, result):
        pass

    prompt = property(fget = _get_prompt)