from src.network import Network

# Testing that the shortest path between two adjacent cities is calculate correctly
def test_get_shortest_path_adjacent():
    net = Network()
    net.make_board()
    
    expected = (['San Francisco', 'Los Angeles'], 3)

    actual = net.get_shortest_path('San Francisco', 'Los Angeles', 3)

    assert actual == expected
