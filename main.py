import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPainter
from tilemap import TileMap
from product import Product, ProductManager
from views.tilemapview import TileMapView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myProductManager = ProductManager()
    myProductManager.initializeProducts()
    view = TileMapView()
    view.show()    
    sys.exit(app.exec())
    