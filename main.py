import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPainter
from tilemap import TileMap
from product import Product, ProductManager
from views.tilemapview import TileMapView, default_store_gen

class ShoppingPathfinder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def initUI(self):
        self.setWindowTitle('Shopping Pathfinder')
        self.setGeometry(100, 100, 800, 600)
        
        label = QLabel('Hello, World!', self)
        label.move(50, 50)
        
        button = QPushButton('Click me!', self)
        button.move(50, 100)
        
        self.show()
        
        
    def paintEvent(self, event):
        self.tilemap.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myProductManager = ProductManager()
    myProductManager.initializeProducts()
    view = TileMapView()
    view.show()    
    sys.exit(app.exec())
    