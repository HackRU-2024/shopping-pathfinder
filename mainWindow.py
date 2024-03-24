from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
                             QListWidgetItem, QStackedWidget, QLineEdit, QListWidget, 
                             QHBoxLayout, QGraphicsScene, QGraphicsView, QMainWindow)
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets
from tilemapview import TileMapView
from product import ProductManager
from pathfinder import Pathfinder
import sys


#from tilemap import TileMap
#list to store products
product_list = []
# Initialize the product manager
myProductManager = ProductManager()
myProductManager.initializeProducts()

class MainWindow(QWidget,):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Demo')

        self.setStyleSheet('''
                MainWindow {
                        background-color: #566981;
                        
                }
                QPushButton {
                        background-color: white;
                        
                }
                * {
                        font-family: 'Arial','Times New Roman';
                }

        ''')
        
        # Create QGraphicsScene
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)

        # Create QGraphicsView
        self.view = QGraphicsView()
        self.view.setScene(self.scene)
        self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        # self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.central_widget(self.view)
        self.zoom_factor = 1.0

        
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        #(1st page) Create pages (widgets) to add to the stacked widget----------
        self.main_page = QWidget()
        # Add labels to each page
        header = QLabel('Main Menu')
        header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #header.setMaximumSize(QtCore.QSize(16777215, 20))
        goto_additem_view_btn = QPushButton('Search Product')
        goto_additem_view_btn.clicked.connect(self.show_addItem_page)
        main_layout = QVBoxLayout(self.main_page)
        main_layout.addWidget(header)
        main_layout.addWidget(goto_additem_view_btn)

        #search product page (widget) ----------
        self.search_product_page = QWidget()

        # line field for user input
        self.user_input_line = QLineEdit()
        self.user_input_line.setMaxLength(10)
        self.user_input_line.setPlaceholderText("Search product")

        #btn to submit str product
        self.add_product_btn = QPushButton('Add')
        self.add_product_btn.clicked.connect(self.add_product_to_list)

        #horizontal layout for user input str function
        user_input_Hbox = QHBoxLayout()
        user_input_Hbox.addWidget(self.user_input_line)
        user_input_Hbox.addWidget(self.add_product_btn)

        #list of input data
        self.product_list_widget = QListWidget()
        self.product_list_widget.setAlternatingRowColors(True)

        #button to switch to tile map
        self.display_tilemap_btn = QPushButton('Map')
        self.display_tilemap_btn.clicked.connect(self.show_tilemap_page)

        # Create buttons to switch to main menu
        self.main_menu_btn = QPushButton('Main Menu')
        self.main_menu_btn.clicked.connect(self.show_mainMenu_page)

        search_product_layout = QVBoxLayout(self.search_product_page)
        search_product_layout.addLayout(user_input_Hbox)
        search_product_layout.addWidget(self.product_list_widget)
        search_product_layout.addWidget(self.display_tilemap_btn)
        search_product_layout.addWidget(self.main_menu_btn)


        #initalizing the tilemap view
        #self.tilemap_page = TileMap()

        # Add pages (qwidgets) to the stacked widget----------- stacking widgets
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.search_product_page)
        #self.stacked_widget.addWidget(self.tilemap_page)

        # Layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        
        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtGui.QKeySequence.ZoomIn),
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_in,
        )

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtGui.QKeySequence.ZoomOut),
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_out,
        )

    def show_mainMenu_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_addItem_page(self):
        self.stacked_widget.setCurrentIndex(1)
    
    #adding to our list & displaying to user
    def add_product_to_list(self):
        #get the str of product & save
        str = self.user_input_line.text()
        if str:
            #if valid string
            product_list.append(str)
            #show in the list widget display
            item = QListWidgetItem(str)
            self.product_list_widget.addItem(item)
            self.user_input_line.clear() #clear
            #check
            #print(self.product_list)
    
    def show_tilemap_page(self):
        view = TileMapView()
        myProductManager.populateShelves(view)
        # Pathfinding
        pathfinder = Pathfinder(view.tilemaps_widget)
        pathfinder.add_node((0, 0))
        pathfinder.add_node((19, 19))
        path = pathfinder.find_path()
        view.tilemaps_widget.add_path(path)
        self.stacked_widget.addWidget(view.tilemaps_widget)
        self.stacked_widget.setCurrentIndex(2)
        
    def keyPressEvent(self, event):
    # Zoom in on '+' or '=' key press
        if event.key() == Qt.Key.Key_Plus:
            self.zoom_in()
        
        # Zoom out on '-' key press
        elif event.key() == Qt.Key.Key_Minus:
            self.zoom_out()

    def zoom_in(self):
        self.zoom_factor *= 1.1
        self.view.scale(1.1, 1.1)

    def zoom_out(self):
        self.zoom_factor /= 1.1
        self.view.scale(1/1.1, 1/1.1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())