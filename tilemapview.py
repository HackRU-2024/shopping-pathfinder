from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget
from tilemap import TileMap


def default_store_gen(tilemap: TileMap):
    for y in range(tilemap.height // 4 - 1):
        for x in range(tilemap.width // 2 - 2):
            tilemap.place_object(2 * x + 2, y * 4 + 5, 'shelf_white_double')
    tilemap.place_dec(2, 1, 'cash_register')

class TileMapView(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 700)        
        self.tilemaps_widget = TileMap(30, 25)
        default_store_gen(self.tilemaps_widget)

        # Add widget to layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tilemaps_widget)
        self.setLayout(main_layout)
    
    def getShelves(self):
        return self.tilemaps_widget.get_objects()

