from tilemap import TileMap
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget


def default_store_gen(tilemap: TileMap):
    for y in range(tilemap.height // 4):
        for x in range(tilemap.width // 2 - 2):
            tilemap.place_object(2 * x + 2, 1 + y * 4, 'shelf_white_double')


class TileMapView(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)        
        self.tilemaps_widget = TileMap(20, 20)
        default_store_gen(self.tilemaps_widget)

        # Create and add widgets to stacked widget
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tilemaps_widget)
        self.setLayout(main_layout)