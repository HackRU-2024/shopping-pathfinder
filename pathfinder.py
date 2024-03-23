from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Pathfinder:
    def __init__(self, matrix):
        self.matrix = matrix
        self.grid = Grid(matrix=self.matrix)

    def find_path(self, start, end):
        start = self.grid.node(*start)
        end = self.grid.node(*end)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path, runs = finder.find_path(start, end, self.grid)
        return path
    
pathfinder = Pathfinder([[1, 1, 1], 
                         [1, 1, 1], 
                         [0, 0, 1]])
path = pathfinder.find_path((0, 0), (2, 2))
print(tuple([tuple(i) for i in path]))