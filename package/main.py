from network import Network

def test_network():
    net = Network()
    net.make_board()
    print(net.routes)
    print(len(net.nodes))

def test_dijk():
    net = Network()
    net.make_board()
    print(net.get_shortest_path('New York', 'Los Angeles', 20))

def main():
    test_dijk()

if __name__ == '__main__':
    main()
