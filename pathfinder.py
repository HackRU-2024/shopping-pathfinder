from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from tilemap import TileMap
import numpy as np
from itertools import permutations
import copy


class Pathfinder:
    def __init__(self, tilemap: TileMap):
        self.tilemap = tilemap
        self.matrix = [[True if tilemap.tiles[y][x].traversable else False for x in range(tilemap.width)]
                       for y in range(tilemap.height)]
        self.grid = Grid(matrix=self.matrix)
        self.goals = []

    def add_node(self, goal):
        self.goals.append(self.grid.node(*goal))


    def find_path_(self, node1, node2):
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(node1, node2, self.grid)
        return path

    def find_path(self):
        paths =[]
        for j in list(permutations(self.goals, len(self.goals))):
            paths_single = []
            for i in range(len(j)-1):
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                path, runs = finder.find_path(j[i], j[i+1], self.grid)
                self.grid.cleanup()

                if path is None:
                    print('No path found!')
                    return None
                
                for node in path:
                    paths_single.append(node)
            paths.append(paths_single)
            
        # Return shortest path
        return min(paths, key=len)
