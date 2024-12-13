from dataclasses import dataclass
from typing import Dict, List
import pandas as pd
import sys
from pathlib import Path

"""
util.py contains all of the cards and pieces necessary for the game

"""

@dataclass
class Destination_Card:
    city1: str
    city2: str
    score: int

    def __repr__(self):
        return f'{self.city1} -> {self.city2}: {self.score}'

class Destination_Deck():
    def __init__(self):
        self.deck: List[Destination_Card] = self.make_deck()

    def make_deck(self) -> List[Destination_Card]:
        deck = []
        # Setting up file pathing
        data_path = Path(__file__).resolve().parent.parent / 'data' / 'tickets.csv'
        
        df = pd.read_csv(data_path)

        for index, row in df.iterrows():
            cur_card = Destination_Card(row['City A'], row['City B'], row['Points'])
            deck.append(cur_card)
        
        return deck


class Train_Deck():
    def __init__(self):
        self.deck: Dict[str, int] = self.make_deck()

    def make_deck(self) -> Dict[str, int]:
        deck = {}
        # Add rainbow cards to deck, using character reps. rainbow becomes 'Z'
        deck['Z'] = 14
        train_colors = ['P', 'W', 'B', 'Y', 'O', 'K', 'R', 'G']
        for color in train_colors:
            deck[color] = 12

        return deck
