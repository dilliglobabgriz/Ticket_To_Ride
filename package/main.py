from network import Network

def test_network():
    net = Network()
    net.make_board()
    print(net.routes)
    print(len(net.routes))

def test_dijk():
    net = Network()
    net.make_board()
    print(net.get_shortest_path('New York', 'Los Angeles', 20))
    print(net.get_shortest_path('Vancouver', 'Miami', 21))
    print(net.edges)



def main():
    test_dijk()

if __name__ == '__main__':
    main()
