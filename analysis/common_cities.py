from src.util import Destination_Deck
from src.network import Network, Route
from src.algorithms import GraphAlgorithms

"""
Common cities looks at which cities are most prevelant in the destination card deck
"""

def most_common_dest_deck_cities():
    cities_count = {}
    d = Destination_Deck()
    deck = d.deck

    for card in deck:
        cities_count[card.city1] = cities_count.setdefault(card.city1, 0) + 1
        cities_count[card.city2] = cities_count.setdefault(card.city1, 0) + 1

    cities_by_use_descending = sorted(cities_count, key=cities_count.get, reverse=True)

    print('Number of appearance for each city in the Destination Card deck')
    for city in cities_by_use_descending:
        print(f'{city}: {cities_count[city]}')

"""
Use dijkstra's to find the shortest path for each given destination card
1. Create a dictionary containing each possible direct route between two cities with a value of 0
2. For each destination card, find the shortest path and increment each direct route on that path
3. 
"""
def most_common_direct_route():
    direct_route_counts = {}
    net = Network()
    net.make_board()

    for edge in net.edges_no_color:
        # Convert edge from list to string
        str_edge = f'{edge[0]} -> {edge[1]}'
        direct_route_counts[str_edge] = 0

    d = Destination_Deck()
    deck = d.deck
    GA = GraphAlgorithms()

    for card in deck:
        cur_path = GA.dijkstras(card.city1, card.city2, net.graph)[1]
        for i in range(len(cur_path)):
            cur_connection_str = f''
            direct_route_counts[cur_connection_str] += 1

    sorted_routes = sorted(direct_route_counts.items(), key=lambda x: x[1], reverse=True)

    for route, count in sorted_routes:
        print(f'Route: {route}, Count: {count}')
    

def main():
    most_common_direct_route()

if __name__ == "__main__":
    main()