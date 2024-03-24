import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPainter
from tilemap import TileMap
from product import Product, ProductManager
from views.tilemapview import TileMapView
from pathfinder import Pathfinder


if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)
    # Initialize the product manager
    myProductManager = ProductManager()
    myProductManager.initializeProducts()
    
    # Create the tilemap view
    view = TileMapView()
    myProductManager.populateShelves(view)
    # Pathfinding
    pathfinder = Pathfinder(view.tilemaps_widget)
    path = pathfinder.find_path((0, 0), (19, 19))
    path = [tuple(i) for i in path]
    view.tilemaps_widget.set_path(path)

    view.show()    
    sys.exit(app.exec())
    