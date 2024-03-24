from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from tilemap import TileMap
import numpy as np


class Pathfinder:
    def __init__(self, tilemap: TileMap):
        matrix = [[True if tilemap.tiles[y][x].traversable else False for x in range(tilemap.width)]
                       for y in range(tilemap.height)]
        self.grid = Grid(matrix=matrix)
        print(np.array(matrix))

    def find_path(self, start, end):
        start = self.grid.node(*start)
        end = self.grid.node(*end)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(start, end, self.grid)
        return path
