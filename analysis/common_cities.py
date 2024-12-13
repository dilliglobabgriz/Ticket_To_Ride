from src.util import Destination_Deck

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

# Use dijkstra's to find the shortest path for each given destination card
def shortest_paths():
    pass
    

def main():
    most_common_dest_deck_cities()

if __name__ == "__main__":
    main()