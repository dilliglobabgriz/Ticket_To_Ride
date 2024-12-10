from network import Network

def test_network():
    net = Network()
    net.make_board()
    print(net.routes)
    print(len(net.nodes))

def main():
    test_network()

if __name__ == '__main__':
    main()
