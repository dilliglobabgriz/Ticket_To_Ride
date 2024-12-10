from typing import List, Tuple, Dict
from dataclasses import dataclass
import pandas as pd
from pathlib import Path
import sys
import heapq

"""
network.py deals with the graph theory for Ticket 2 Ride
Contains 33 cities (nodes) and _ routes (edges)
"""

@dataclass
class Route:
    city1: str
    distance: int
    color: str
    city2: str

class Network():
    def __init__(self):
        self.nodes: List[str] = []
        self.edges: List[Route] = []
        self.location: str = 'USA'
        self.graph: Dict[str, Dict[str, int]] = {}

    def make_board(self) -> None:
        if self.location == 'USA':
            self.make_board_usa()
        
        self.graph = self.build_graph()

    def build_graph(self) -> Dict[str, Dict[str, int]]:
        graph = {}
        for edge in self.edges:
            # Unpack edge
            C1, distance, _, C2 = edge.city1, edge.distance, edge.color, edge.city2
            if C1 not in graph:
                graph[C1] = {}
            if C2 not in graph:
                graph[C2] = {}
            graph[C1][C2] = distance
            graph[C2][C1] = distance
        return graph


    def make_board_usa(self) -> None:
        self.nodes = [
            'Atlanta','Boston','Calgary','Charleston','Chicago','Dallas','Denver',
            'El Paso','Houston','Kansas City','Las Vegas','Little Rock','Los Angeles',
            'Miami','Montreal','Nashville','New Orleans','New York','Oklahoma City',
            'Phoenix','Pittsburgh','Portland','Raleigh','Salt Lake City','San Francisco',
            'Santa Fe','Sault St. Marie','Seattle','St. Louis','Toronto','Vancouver',
            'Washington','Winnipeg'
        ]

        self.edges = self.get_edges_usa()

    def get_edges_usa(self) -> List[Route]:
        route_list: List[Route] = []

        # Setting up file pathing
        data_path = Path(__file__).resolve().parent.parent / 'data' / 'routes.csv'
        
        df = pd.read_csv(data_path)
        
        # Iterate over each row and turn data into type Route, then append to return list
        for index, row in df.iterrows():
            cur_route = Route(row['City A'], row['Distance'], row['Color'], row['City B'])
            route_list.append(cur_route)

        return route_list

    def get_shortest_path(self, C1: str, C2: str, score: int) -> Tuple[List[str], int]:
        shortest_path, path_length = self.dijkstras(C1, C2)
        return shortest_path, path_length

    def dijkstras(self, start, end):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            cost, cur_city, path = heapq.heappop(queue)
            if cur_city in visited:
                continue

            path = path + [cur_city]
            visited.add(cur_city)

            if cur_city == end:
                return cost, path

            for neighbor, weight in self.graph[cur_city].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return "Error, no path available"
