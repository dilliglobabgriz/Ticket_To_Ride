import pytest
from package.network import Network

def test_get_color():
    n = Network()
    n.make_board()
    color = n.get_color('Duluth', 'Helena')

    assert color == 'O'

def test_get_distance():
    n = Network()
    n.make_board()
    distance = n.get_distance('Duluth', 'Helena')

    assert distance == 6
