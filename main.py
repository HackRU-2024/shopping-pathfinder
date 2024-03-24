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
    myProductManager
    # Pathfinding
    pathfinder = Pathfinder(view.tilemaps_widget)
    pathfinder.add_node((29, 24)) # Start
    pathfinder.add_node(myProductManager.get_product('sesame seeds')['Location'])
    pathfinder.add_node(myProductManager.get_product('vinegar')['Location'])
    pathfinder.add_node(myProductManager.get_product('hot sauce')['Location'])
    pathfinder.add_node((2, 2))
    path = pathfinder.find_path()
    view.tilemaps_widget.add_path(path)

    view.show()    
    sys.exit(app.exec())
    