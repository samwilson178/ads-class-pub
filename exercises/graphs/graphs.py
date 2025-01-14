#!/usr/bin/env python3
"""
`graphs` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import heapq
import pathlib
import sys


class Vertex:
    """Graph vertex"""

    def __init__(self, key):
        """Graph constructor"""
        self._key = key
        self._neighbors = {}
        self._distance = sys.maxsize
        self._previous = None
        self._color = "white"
        self._discovered = 0
        self._colored = 0

    def get_key(self):
        """Get node key"""
        return self._key

    key = property(get_key)

    def get_neighbor(self, other: str):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other: str, weight: int = 0):
        """Add neighbor"""
        self._neighbors[other] = weight

    neighbor = property(get_neighbor, set_neighbor)

    def get_all_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.keys()

    all_neighbors = property(get_all_neighbors)

    def get_distance(self):
        """Get distance"""
        return self._distance

    def set_distance(self, distance: int):
        """Set distance"""
        self._distance = distance

    distance = property(get_distance, set_distance)

    def get_previous(self):
        """Get previous"""
        return self._previous

    def set_previous(self, previous):
        """Set previous"""
        self._previous = previous

    previous = property(get_previous, set_previous)

    def get_color(self):
        """Get color"""
        return self._color

    def set_color(self, color: str):
        """Get color"""
        self._color = color

    color = property(get_color, set_color)

    def get_discovery(self):
        """Get discovery time"""
        return self._discovered

    def set_discovery(self, time_value):
        """Set discovery time"""
        self._discovered = time_value

    discovered = property(get_discovery, set_discovery)

    def get_finish(self):
        """Get finish time"""
        return self._colored

    def set_finish(self, time_value):
        """Set finish time"""
        self._colored = time_value

    finished = property(get_finish, set_finish)

    def get_weight(self, other):
        """Get edge weight"""
        return self._neighbors[other]

    def __str__(self):
        """Print a vertex"""
        return (
            "Neighbors of "
            + str(self._key)
            + ": "
            + str([x.key for x in self._neighbors])
        )

    def __lt__(self, other):
        return self._key < other.key


class Graph:
    """Graph class"""

    def __init__(self):
        """Create a new, empty graph"""
        self.vertices = {}
        self.time = 0

    def add_vertex(self, key: str) -> None:
        """Add an instance of Vertex to the graph"""
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int = 0) -> None:
        """Add a new, weighted, directed edge to the graph that connects two vertices"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].set_neighbor(self.vertices[to_vertex], weight)

    def get_vertex(self, key: str) -> Vertex:
        """Find the vertex in the graph named vert_key"""
        return self.vertices.get(key, None)

    def get_vertices(self) -> list[Vertex]:
        """Return the list of all vertices in the graph"""
        return self.vertices.keys()

    def reset_distances(self) -> None:
        """Reset distances to test Dijkstra's"""
        for a_vertex in self:
            a_vertex.set_distance(sys.maxsize)

    def __contains__(self, key: str) -> bool:
        """
        Testing the belonging: vertex in graph
        Return True, if the given vertex is in the graph
        Return False, if the given vertex is NOT in the graph"""
        return key in self.vertices

    def __iter__(self):
        """Iterator"""
        return iter(self.vertices.values())

    def __len__(self) -> int:
        """Graph's size"""
        # TODO: Implement this method
        return len(self.vertices)
        ...

    def hub(self) -> Vertex:
        """Find a Vertex with the most outgoing edges"""
        # TODO: Implement this method
        max_vertex = Vertex('foo')
        for key in self.vertices.keys():
            vertex = self.vertices[key]
            if len(vertex.all_neighbors) > len(max_vertex.all_neighbors):
                max_vertex = vertex
        return max_vertex.key
        ...

    def size(self) -> int:
        """Find the number of edges in a Graph"""
        # TODO: Implement this method
        count = 0
        used = []
        for key in self.vertices.keys():
            vertex = self.vertices[key]
            used.append(vertex)
            for neighbor in vertex.all_neighbors:
                if neighbor not in used:
                    count += 1
        return count
        ...

    def dijkstra(self, start: Vertex) -> None:
        """Dijkstra's shortest path algorithm"""
        start.distance = 0
        pq = [[start.distance, start]]
        heapq.heapify(pq)
        while len(pq) > 0:
            current_vertex = heapq.heappop(pq)[1]
            for next_vertex in current_vertex.all_neighbors:
                new_distance = current_vertex.distance + current_vertex.get_weight(
                    next_vertex
                )
                if new_distance < next_vertex.distance:
                    next_vertex.distance = new_distance
                    next_vertex.previous = current_vertex
                    found = False
                    for v in pq:
                        if v[1].key == next_vertex.key:
                            v[0] = next_vertex.distance
                            heapq.heapify(pq)
                            found = True
                    if not found:
                        heapq.heappush(pq, [next_vertex.distance, next_vertex])




def build_graph(filename: str) -> Graph:
    g = Graph()
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            src, dst, cost = line.strip().split(",")
            g.add_edge(src, dst, int(cost))
    return g


def main():
    """Main function"""
    filename = "network.txt"
    if not pathlib.Path(filename).exists():
        filename = f"exercises/graphs/{filename}"
    g = build_graph(filename)
    v = g.get_vertex("t")
    print(f"Searching from {v.key}")
    g.dijkstra(v)
    g.reset_distances()
    v = g.get_vertex("x")
    print(f"Searching from {v.key}")
    g.dijkstra(v)


if __name__ == "__main__":
    main()
