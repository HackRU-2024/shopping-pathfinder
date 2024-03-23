import pytest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from tilemap import Tile, TileMap

app = QApplication([])

class TestTileMap:
    @pytest.fixture
    def tile_map(self):
        return TileMap(10, 10)

    def test_init(self, tile_map):
        assert tile_map.width == 10
        assert tile_map.height == 10
        assert tile_map.tile_size == 32
        assert isinstance(tile_map.tiles[0][0], Tile)
        assert tile_map.tiles[0][0].type == 'floor_concrete'
        assert tile_map.tiles[0][0].traversable
        assert isinstance(tile_map.texture_atlas, QPixmap)

    def test_get_tile_texture(self, tile_map):
        texture = tile_map.get_tile_texture('floor_concrete')
        assert isinstance(texture, QPixmap)

    def test_get_obj_texture_size(self, tile_map):
        texture, offset = tile_map.get_obj_texture_size('shelf_white_single_0')
        assert isinstance(texture, QPixmap)
        assert isinstance(offset, tuple)