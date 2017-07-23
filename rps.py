"""
This isn't a very interesting one and hardly has anything to do with SO. I was
just on the question index and saw a question about someone having trouble with
a rock paper scissors game, and I realized I'd never written one myself, so I 
decided to have my try at it. Here it is.
"""
from getpass import getpass
from random import choice
import unittest


class RPSException(Exception):
    pass


class Move(object):
    """
    Represents a move that a player can make. i.e `Rock`, `Paper`, `Scissors`
    """
    def __init__(self, name, strength, weaknesses):
        self.name = name
        self.strength = strength
        self.weaknesses = weaknesses

    def __gt__(self, other):
        if other.strength in self.weaknesses + [self.strength]:
            return False 
        return True

    def __eq__(self, other):
        return self.strength == other.strength


class Player(object):
    def __init__(self, name):
        self.name = name

    def play_rps(self, choices):
        return choice(choices)

    def __str__(self):
        return self.name


class Game(object):
    def __init__(self, choices, player1, player2):
        self.move_mapping = self._get_move_mapping(choices)
        self.choices = choices
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def _get_move_mapping(self, choices):
        by_full_name = {c.name.lower(): c for c in choices}
        by_first_letter = {c.name[0].lower(): c for c in choices}
        return {**by_full_name, **by_first_letter}

    def play(self):
        p1_choice = None
        p2_choice = None

        while p1_choice is None:
            try:
                p1_choice = self.get_player_move(self.player1)
            except RPSException as e:
                print(e)

        while p2_choice is None:
            try:
                p2_choice = self.get_player_move(self.player2)
            except RPSException as e:
                print(e)

        if p1_choice > p2_choice:
            self.player1_score += 1
            winner = self.player1.name
        elif p1_choice < p2_choice:
            self.player2_score += 1
            winner = self.player2.name
        else:
            winner = 'No one'
        self._print_score()
        return winner

    def _print_score(self):
        score_message = "Current Score\nPlayer 1({p1_name}):\t{p1_score}\nPlayer 2({p2_name}):\t {p2_score}\n".format(
                p1_name=self.player1.name, p1_score=self.player1_score, p2_name=self.player2.name, p2_score=self.player2_score)
        print(score_message)

    def get_player_move(self, player):
        prompt = "{}, enter your move: ".format(player.name)
        move = getpass(prompt=prompt)
        if move.lower() not in self.move_mapping:
            raise RPSException("That's not a valid move. Please choose from one of the following: {}".format(', '.join(self.move_mapping.keys())))
        else:
            return self.move_mapping[move.lower()]
        


class TestMoves(unittest.TestCase):
    def setUp(self):
        self.rock = Move('Rock', 0, [1])
        self.paper = Move('Paper', 1, [2]) 
        self.scissors = Move('Scissors', 2, [0])

    def test_rock_v_paper(self):
        comparison1 = self.rock > self.scissors
        comparison2 = self.rock < self.scissors
        self.assertTrue(comparison1)
        self.assertFalse(comparison2)

    def test_paper_v_scissors(self):
        comparison1 = self.paper < self.scissors
        comparison2 = self.paper > self.scissors
        self.assertTrue(comparison1)
        self.assertFalse(comparison2)


if __name__ == '__main__':
    # unittest.main()
    player1 = Player('Cory')
    player2 = Player('Joe')
    rock = Move('Rock', 0, [1])
    paper = Move('Paper', 1, [2]) 
    scissors = Move('Scissors', 2, [0])
    moves = [rock, paper, scissors]
    game = Game(moves, player1, player2)
    for x in range(5):
        game.play()

