import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QPainter
from tilemap import TileMap
from product import Product

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
    widget = TileMap(40, 25)
    widget.set_tile(5, 5, 'floor_wood')
    widget.place_object(2, 2, 'shelf_white_single_0')
    widget.place_object(3, 3, 'shelf_white_single_1')
    widget.place_object(3, 4, 'shelf_white_single_1')
    widget.place_object(4, 4, 'shelf_white_double')
    widget.place_object(6, 4, 'shelf_white_double')
    # widget.place_object(5, 3, 'shelf_white_double')
    widget.show()
    sys.exit(app.exec())
    