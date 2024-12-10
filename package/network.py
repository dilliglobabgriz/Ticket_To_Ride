from typing import List
from dataclasses import dataclass
import pandas as pd
from pathlib import Path

"""
network.py deals with the graph theory for Ticket 2 Ride
Contains 33 cities (nodes) and _ routes (edges)
"""

@dataclass
class Route:
    city1: str
    distnace: int
    color: str
    city2: str

class Network():
    def __init__(self):
        self.nodes: List[str] = []
        self.routes: List[Route] = []
        self.location: str = 'USA'

    def make_board(self) -> None:
        if self.location == 'USA':
            self.make_board_usa()

    def make_board_usa(self) -> None:
        self.nodes = [
            'Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver',
            'El Paso','Houston','Kansas City','Las Vegas','Little Rock','Los Angeles',
            'Miami','Montreal','Nashville','New Orleans','New York','Oklahoma City',
            'Phoenix','Pittsburgh','Portland','Raleigh','Salt Lake City','San Francisco',
            'Santa Fe','Sault St. Marie','Seattle','St. Louis','Toronto','Vancouver',
            'Washington','Winnipeg'
        ]

        self.routes = self.get_routes_usa()

    def get_routes_usa(self) -> List[Route]:
        route_list: List[Route] = []

        # Setting up file pathing
        data_path = Path(__file__).resolve().parent.parent / 'data' / 'routes.csv'
        
        df = pd.read_csv(data_path)
        
        # Iterate over each row and turn data into type Route, then append to return list
        for index, row in df.iterrows():
            cur_route = Route(row['City A'], row['Distance'], row['Color'], row['City B'])
            route_list.append(cur_route)

        return route_list