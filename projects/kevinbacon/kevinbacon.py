#!/usr/bin/env python3
"""
`kevinbacon` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.11
"""

import argparse
import pathlib
import sys
import time

from pythonds3.graphs import Graph


def read_file(filename: str) -> Graph:
    """Build a graph from the file"""
    the_graph: Graph = Graph()
    # TODO: Implement this function
    movies = {}
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            movie,actor = line.split('|')
            if movie not in movies.keys():
                movies[movie] = [actor]
            else:
                movies[movie].append(actor)
    for movie in movies.keys():
        for from_actor in movies[movie]:
            for to_actor in movies[movie]:
                if from_actor != to_actor:
                    the_graph.add_edge(from_actor,to_actor,movie)
    return the_graph
    ...


def find_max_kbn_actors(graph: Graph) -> list[str]:
    """Find actor(s) with the highest KBN value"""
    # TODO: Implement this function
    max_actors = []
    max_distance = 0
    for actor in graph._vertices.keys():
        if graph._vertices[actor].distance == sys.maxsize:
            pass
        elif graph._vertices[actor].distance > max_distance:
            max_actors = [actor]
            max_distance = graph._vertices[actor].distance
        elif graph._vertices[actor].distance == max_distance:
            max_actors.append(actor)
    return max_actors
    ...


def main():
    """Main function"""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("actor", type=str, nargs="*")
    args = argparser.parse_args()

    print("Kevin Bacon number calculator")
    print("Reading the file")
    time_start = time.time()
    filename = "movie_actors_full.txt"
    if not pathlib.Path(filename).exists():
        filename = f"projects/kevinbacon/{filename}"
    the_graph = read_file(filename)
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"File read in {elapsed:.2f} sec")
    print()

    print("Analyzing the graph")
    connections = 0
    for vertex in the_graph:
        connections = connections + len(vertex.get_neighbors())
    print(f"There are {len(the_graph)} connected actors in the file")
    print(f"There are {connections} connections between actors in the file")
    print()

    print("Finding paths")
    kevin = the_graph.get_vertex("Kevin Bacon")
    time_start = time.time()
    the_graph.bfs(kevin)
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"Paths found in {elapsed:.2f} sec")
    print()

    print("Looking for actors with the highest Kevin Bacon number")
    time_start = time.time()
    high_kbn_lst = find_max_kbn_actors(the_graph)
    time_end = time.time()
    elapsed = time_end - time_start
    print(f"{len(high_kbn_lst)} actor(s) found in {elapsed:.2f} sec")
    print(
        "The following actor(s) have the Kevin Bacon number of "
        + f"{the_graph.get_vertex(high_kbn_lst[0]).get_distance()}:"
    )
    for name in high_kbn_lst:
        print(name)
    print()

    actor = " ".join(args.actor) or high_kbn_lst[0]
    # TODO: Keep asking the user to enter a name until the user enters an empty line
    while True:
        actor = input("What Actor would you like to trace? (exit to exit) ")
        if actor == 'exit':
            break
        if not the_graph.get_vertex(actor):
            print('Invalid Input, try again')
        else:
            distance = the_graph.get_vertex(actor).get_distance()
            path = []
            current = the_graph.get_vertex(actor)
            while current:
                path.append(current)
                current = current.previous
            for i in range(len(path)-1):
                print(f'{i+1}) {path[i].key} acted with {path[i+1].key} in {the_graph._edges[(path[i].key,path[i+1].key)]}')
            print(f"{actor}'s Kevin Bacon number is {distance}")
    ...


if __name__ == "__main__":
    main()
