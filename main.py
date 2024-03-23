import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from tilemap import TileMap
from product import Product

class ShoppingPathfinder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.tilemap = TileMap(20, 20, 32)
        
    
    def initUI(self):
        self.setWindowTitle('Shopping Pathfinder')
        self.setGeometry(100, 100, 800, 600)
        
        label = QLabel('Hello, World!', self)
        label.move(50, 50)
        
        button = QPushButton('Click me!', self)
        button.move(50, 100)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShoppingPathfinder()
    sys.exit(app.exec())
    