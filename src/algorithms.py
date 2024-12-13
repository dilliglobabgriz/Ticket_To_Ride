import heapq

class GraphAlgorithms():
    def dijkstras(self, start, end, graph):
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

            for neighbor, weight in graph[cur_city].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return "Error, no path available"