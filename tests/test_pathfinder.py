from pathfinder import Pathfinder

def test_find_path():
    matrix = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1]
    ]
    pathfinder = Pathfinder(matrix)
    
    # Test case 1: Path exists between two points
    start = (0, 0)
    end = (2, 2)
    path = pathfinder.find_path(start, end)
    print(path.__repr__())
    assert [tuple(i) for i in path] == [(0, 0), (1, 1), (2, 2)]

    # Test case 2: Path does not exist between two points
    start = (0, 0)
    end = (0, 2)
    path = pathfinder.find_path(start, end)
    assert path == []
