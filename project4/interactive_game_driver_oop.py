from interactive_game import InteractiveGame
from bagels import Bagels

class InteractiveGameDriver:
    def __init__(self, game):
        if not isinstance(game, InteractiveGame):
            raise ValueError('Invalid game instance')
        self._game = game

    def play(self):
        print(self._game.get_instruction())

        while self._game.can_continue():
            print(self._game.get_status())

            guess = input(self._game.prompt)
            try:
                valid_guess = self._game.validate(guess)
                result, hint = self._game.evaluate(valid_guess)

                if result:
                    break
                elif hint is not None:
                    print(hint)

            except ValueError as err:
                print(err)

        print(self._game.respond(result))


if __name__ == '__main__':
    dr = InteractiveGameDriver(Bagels())
    dr.play()