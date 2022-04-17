__all__ = ['hangman']

from hangman.the_hangman import Hangman


def hangman():
    game = Hangman()

    while game.guesses != 0:
        print(f"{game.display_answer} | Guessed: {game.guessed} | Lives left: {game.guesses}")
        guess = input("Enter a letter or guess: ")

        if not guess.isalpha():
            print("Yo that's not a letter, try again!")
            continue
        else:
            game.handle_input(guess.lower())
            if game.won:
                return
            else:
                continue

    print(f"The correct answer was '{game.answer}'! Thanks for playing :D")


if __name__ == '__main__':
    hangman()
    