from enum import Enum
import pprint
import random

class Suit(Enum):
    HEARTS = "HEARTS"
    CLUBS = "CLUBS"
    SPADES = "SPADES"

class Number(Enum):
    TWO = 2
    THREE = 3

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.owner = None

    def __repr__(self):
        return "Card " + str(self.suit) + " " + str(self.number) + ' (owner: {})'.format(str(self.owner)) + "\n"

    def set_owner(self, name):
        self.owner = name


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.knowledge = None
        self.hand = hand
        self.update_card_owners()

    def __repr__(self):
        return "\n Player " + str(self.name) + "\n " + str(self.hand)

    def update_card_owners(self):
        for card in self.hand:
            card.set_owner(self.name)

class Game:
    def __init__(self, number_of_players, hand_limit, player_names,
                 initial_deck):
        self.number_of_players = number_of_players
        self.hand_limit = hand_limit
        self.player_names = player_names
        self.initial_deck = initial_deck
        self.trump_card = 0
        self.trump_suit = 0
        self.turns_taken = 0

    def set_trump_card(self, card):
        self.trump_card = card
        self.trump_suit = card.suit


card_list = list()

for suit in Suit:
    for number in Number:
        card_list.append(Card(suit, number))

#### GAME DETAILS ###
number_of_players = 3
hand_limit = 1

player_names = ["boris", "marieke", "ludi"]
players = {}

#random.shuffle(card_list)   # schudden

game = Game(number_of_players, hand_limit, player_names,
                 card_list)
print(card_list)

for player in player_names:
    hand = card_list[0:hand_limit]
    players[player] = Player(player, hand)
    del card_list[0:hand_limit]

## initialize pot ##
players["pot"] = Player("pot", card_list)

print(players)

# find trump card
trump_card = players["pot"].hand[0]
game.set_trump_card(trump_card)
print(game.trump_suit)

## implement fir











