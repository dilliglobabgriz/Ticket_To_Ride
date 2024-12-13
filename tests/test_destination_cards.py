from src.util import Destination_Deck
import pytest

def test_dest_deck_creation():
    d = Destination_Deck()
    length = len(d.deck)

    assert length == 30