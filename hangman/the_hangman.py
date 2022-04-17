__all__ = ["Hangman"]

import random
from typing import List

from english_words import english_words_lower_alpha_set


class Hangman:
    def __init__(self):
        self._answer: str = random.choice(list(english_words_lower_alpha_set))
        self._guessed: List[str] = []
        self._guesses: int = 6
        self._display_answer = ["-"] * len(self._answer)
        self._won = False

    @property
    def answer(self):
        return self._answer

    @property
    def display_answer(self):
        return "".join(self._display_answer)

    @property
    def guessed(self):
        return sorted(self._guessed)

    @property
    def guesses(self):
        return self._guesses

    @property
    def won(self):
        return self._won

    def _handle_correct_letter(self, letter):
        for i, char in enumerate(self._answer):
            if letter == char:
                self._display_answer[i] = letter

        if self.display_answer == self._answer:
            self._handle_win()

    def _handle_guess(self, guess: str):
        if guess == self._answer:
            self._handle_win()
        else:
            self._guesses -= 1
            print("Nope, wrong answer!")

    def handle_input(self, guess: str):
        if len(guess) == 1:
            self._handle_letter(guess)
        else:
            self._handle_guess(guess)

    def _handle_letter(self, letter: str):
        if letter in self._guessed:
            print(f"Already guessed {letter}")
        else:
            self._guessed.append(letter)
            if letter in self._answer:
                self._handle_correct_letter(letter)
            else:
                self._guesses -= 1
                print(f"Sorry, {letter} isn't in the answer!")

    def _handle_win(self):
        print(f"'{self._answer}' is correct! You win! Thanks for playing :D")
        self._won = True
