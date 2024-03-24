from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from tilemap import TileMap
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
        #grind = Grid(matrix=copy.deepcopy(self.matrix))

        for i in range(len(self.goals)-1):
            finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
            path, runs = finder.find_path(self.goals[i], self.goals[i+1], self.grid)
            self.grid.cleanup()

            if path is None:
                print('No path found!')
                return None
            
            for node in path:
                paths.append(node)
        
        return paths
