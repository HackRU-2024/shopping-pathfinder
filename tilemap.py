
class TileMap:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                tile = self.tiles[y][x]
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(surface, (tile * 255, tile * 255, tile * 255), rect)

    def set_tile(self, x, y, tile):
        self.tiles[y][x] = tile

    def get_tile(self, x, y):
        return self.tiles[y][x]