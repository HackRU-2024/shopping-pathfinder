from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt, QRect


tile_mappings = {
    'floor_concrete' : QRect(192, 928, 32, 32),
    'floor_wood' : QRect(0, 1056, 32, 32),
}
# Object mappings are a dictionary of object names to a tuple of a QRect and a tuple of offsets.
obj_mappings = {
    'shelf_white_single_0': (QRect(64, 592, 32, 62), (0, -30)),
    'shelf_white_single_1': (QRect(96, 592, 32, 62), (0, -30)),
    'shelf_white_double': (QRect(128, 592, 64, 64), (0, -32)),
}


class Tile:
    def __init__(self, tile_type: str, traversable: bool):
        self.type = tile_type
        self.traversable = traversable
        self.products = []


class TileMap(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.tile_size = 32
        self.tiles = [[Tile('floor_concrete', True) for _ in range(width)] for _ in range(height)]
        self.objects = []
        self.texture_atlas = QPixmap('assets/modern_tiles/interiors_free/32x32/Interiors_free_32x32.png')


    def get_tile_texture(self, tile_type: str):
        return self.texture_atlas.copy(tile_mappings[tile_type])


    def get_obj_texture_size(self, obj_type: str):
        '''Return the texture and the offset of the object texture.'''
        texture, offset = obj_mappings[obj_type]
        return self.texture_atlas.copy(texture), offset


    def paintEvent(self, Event):
        painter = QPainter(self)
        # Paint tiles
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x].type
                texture = self.get_tile_texture(tile_type)
                painter.drawPixmap(x * self.tile_size, y * self.tile_size, texture)

        # Paint objects
        for object in self.objects:
            x, y, obj_type = object
            texture, offset = self.get_obj_texture_size(obj_type)
            painter.drawPixmap(x * self.tile_size + offset[0], y * self.tile_size + offset[1], texture)


    def set_tile(self, x, y, tile):
        self.tiles[y][x].type = tile


    def get_tile(self, x, y):
        return self.tiles[y][x]
    

    def place_object(self, x, y, obj_type):
        self.objects.append((x, y, obj_type))

    def get_objects(self):
        return self.objects
        
        
    def add_product(self, x, y, product):
        self.tiles[y][x].products.append(product)
