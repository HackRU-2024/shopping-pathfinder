from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt, QRect

class TileMap(QWidget):
    def __init__(self, width, height, tile_size):
        super().__init__()
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [['tile_basic' for _ in range(width)] for _ in range(height)]
        self.texture_atlas = QPixmap('assets/modern_tiles/interiors_free/32x32/Interiors_free_32x32.png')
        print(self.texture_atlas.width())


    def get_tile_texture(self, tile_type: str):
        if tile_type == 'tile_basic':
            return self.texture_atlas.copy(QRect(192, 928, 32, 32))
        else:
            return None

    def paintEvent(self, Event):
        painter = QPainter(self)
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x]
                texture = self.get_tile_texture(tile_type)
                painter.drawPixmap(x * self.tile_size, y * self.tile_size, texture)

    def set_tile(self, x, y, tile):
        self.tiles[y][x] = tile

    def get_tile(self, x, y):
        return self.tiles[y][x]