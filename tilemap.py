from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class TileMap(QWidget):
    def __init__(self, width, height, tile_size):
        super().__init__()
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]

    def paintEvent(self, Event):
        painter = QPainter(self)
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x]
                if tile_type == 0:
                    painter.fillRect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size,
                                     QColor(Qt.GlobalColor.black))
                elif tile_type == 1:
                    painter.fillRect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size,
                                     QColor(Qt.GlobalColor.white))

    def set_tile(self, x, y, tile):
        self.tiles[y][x] = tile

    def get_tile(self, x, y):
        return self.tiles[y][x]