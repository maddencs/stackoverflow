"""
This isn't a very interesting one and hardly has anything to do with SO. I was
just on the question index and saw a question about someone having trouble with
a rock paper scissors game, and I realized I'd never written one myself, so I 
decided to have my try at it. Here it is.
"""
from random import choice
import unittest

class Move(object):
    """
    Represents a move that a player can make. i.e `Rock`, `Paper`, `Scissors`
    """
    def __init__(self, name, strength, weakness):
        self.name = name
        self.strength = strength
        self.weakness = weakness

    def __gt__(self, other):
        if other.strength == self.weakness:
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
        self.choices = choices
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def play(self):
        p1_choice = self.player1.play_rps(self.choices)
        p2_choice = self.player2.play_rps(self.choices)
        if p1_choice > p2_choice:
            self.player1_score += 1
            return self.player1
        elif p1_choice < p2_choice:
            self.player2_score += 1
            return self.player2
        else:
            return 'No one'


class TestMoves(unittest.TestCase):
    def setUp(self):
        self.rock = Move('Rock', 0, 1)
        self.paper = Move('Paper', 1, 2) 
        self.scissors = Move('Scissors', 2, 0)

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
    rock = Move('Rock', 0, 1)
    paper = Move('Paper', 1, 2) 
    scissors = Move('Scissors', 2, 1)
    moves = [rock, paper, scissors]
    game = Game(moves, player1, player2)
    for x in range(15):
        print("{} wins!".format(game.play()))
    print("Player 1 Final Score:\t{}\nPlayer 2 Final Score:\t{}\n".format(
        game.player1_score, game.player2_score))

