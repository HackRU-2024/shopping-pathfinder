from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPixmap, QPen
from PyQt6.QtCore import Qt, QRect

tile_mappings = {
    'floor_concrete' : QRect(192, 928, 32, 32),
    'floor_wood' : QRect(0, 1056, 32, 32),
}
# Object mappings are a dictionary of object names to a tuple of a QRect and a tuple of offsets.
obj_mappings = {
    'shelf_white_single_0': (QRect(64, 592, 32, 62), (0, -30), (0, 0)),
    'shelf_white_single_1': (QRect(96, 592, 32, 62), (0, -30), (0, 0)),
    'shelf_white_double': (QRect(128, 592, 64, 64), (0, -32), (1, 0)),
    'cash_register': (QRect(96, 276, 32, 44), (0, -16), (0, 0)),
    'cash_register_green': (QRect(96, 116, 32, 44), (0, -16), (0, 0)),
    'counter_side_green': (QRect(102, 64, 26, 32), (3, 0), (0, 0)),
    'counter_corner_green': (QRect(32, 96, 58, 36), (0, -4), (1, 0)),
    'shelf_white_double_side': (QRect(449, 782, 32, 96), (0, -64), (0, 1)),
    'tree_medium': (QRect(334, 1426, 36, 68), (-2, -36), (0, 0)),
    'tree_palm': (QRect(426, 1408, 46, 68), (-7, -36), (0, 0)),
}

class Tile:
    def __init__(self, tile_type: str, traversable: bool):
        self.type = tile_type
        self.traversable = traversable


class TileMap(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.tile_size = 32
        self.tiles = [[Tile('floor_concrete', True) for _ in range(width)] for _ in range(height)]
        self.objects = []
        self.decorations =[]
        self.path = []
        self.texture_atlas = QPixmap('assets/modern_tiles/interiors_free/32x32/Interiors_free_32x32.png')


    def get_tile_texture(self, tile_type: str):
        return self.texture_atlas.copy(tile_mappings[tile_type])


    def get_obj_texture_size(self, obj_type: str):
        '''Return the texture and the offset of the object texture.'''
        texture, offset, size = obj_mappings[obj_type]
        return self.texture_atlas.copy(texture), offset


    def paintEvent(self, Event):
        painter = QPainter(self)
        # Paint tiles
        for y in range(self.height):
            for x in range(self.width):
                tile_type = self.tiles[y][x].type
                texture = self.get_tile_texture(tile_type)
                painter.drawPixmap(x * self.tile_size, y * self.tile_size, texture)

        # Paint path
        pen = QPen(QColor(255, 0, 0, 255))
        pen.setWidth(5)
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        if len(self.path) > 1:
            for i in range(len(self.path) - 1):
                x, y = self.path[i]
                next_x, next_y = self.path[i+1]
                painter.drawLine(x * self.tile_size + self.tile_size // 2, y * self.tile_size + self.tile_size // 2,
                                 next_x * self.tile_size + self.tile_size // 2, next_y * self.tile_size + self.tile_size // 2)
                
        # Paint objects
        for object in self.objects:
            x, y, obj_type = object
            texture, offset = self.get_obj_texture_size(obj_type)
            painter.drawPixmap(x * self.tile_size + offset[0], 
                               y * self.tile_size + offset[1], texture)
        for dec in self.decorations:
            x, y, dec_type = dec
            texture, offset = self.get_obj_texture_size(dec_type)
            painter.drawPixmap(x * self.tile_size + offset[0], 
                               y * self.tile_size + offset[1], texture)


    def add_path(self, path):
        for node in path:
            self.path.append(tuple(node))

    def set_tile(self, x, y, tile):
        self.tiles[y][x].type = tile


    def get_tile(self, x, y):
        return self.tiles[y][x]
    

    def place_object(self, x, y, obj_type):
        self.objects.append((x, y, obj_type))
        size = obj_mappings[obj_type][2]
        self.tiles[y][x].traversable = False
        self.tiles[y][x+size[0]].traversable = False
        self.tiles[y+size[1]][x].traversable = False

    def get_objects(self):
        return self.objects
        
        
        
    def place_dec(self, x, y, dec_type):
        self.decorations.append((x, y, dec_type))
        size = obj_mappings[dec_type][2]
        self.tiles[y][x].traversable = False
        self.tiles[y][x+size[0]].traversable = False
        self.tiles[y+size[1]][x].traversable = False
        
        
    def add_product(self, x, y, product):
        self.tiles[y][x].products.append(product)
