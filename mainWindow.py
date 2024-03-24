from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
                             QListWidgetItem, QStackedWidget, QLineEdit, QListWidget, QHBoxLayout, 
                             QGraphicsScene, QGraphicsView, QMainWindow, QMessageBox, QComboBox)
from PyQt6 import QtCore,  QtGui, QtWidgets
from tilemapview import TileMapView
from tilemapview import TileMapView
from product import ProductManager
from pathfinder import Pathfinder
import sys


#from tilemap import TileMap
#list to store products
product_list = []
product_node_list = []
current_dept = None
# Initialize the product manager
myProductManager = ProductManager()
myProductManager.initializeProducts()

class MainWindow(QWidget):
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
        #self.central_widget(self.view)
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
        main_layout.setGeometry(QtCore.QRect(200, 20, 461, 491))

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

        #combobox for shopping by Department
        self.shop_by_department_combobox = QComboBox()
        self.shop_by_department_combobox.currentTextChanged.connect(self.department_selected)

        #list widget display results
        self.search_result_display = QListWidget()
        self.search_result_display.setAlternatingRowColors(True)


        #list of input data
        self.product_list_widget = QListWidget()
        self.product_list_widget.setAlternatingRowColors(True)

        #button to switch to tile map
        self.display_tilemap_btn = QPushButton('Map')
        self.display_tilemap_btn.setContentsMargins(10, 10, 10, 10)
        self.display_tilemap_btn.clicked.connect(self.show_tilemap_page)

        # Create buttons to switch to main menu
        self.main_menu_btn = QPushButton('Main Menu')
        self.main_menu_btn.clicked.connect(self.show_mainMenu_page)

        search_product_layout = QVBoxLayout(self.search_product_page)
        search_product_layout.setSpacing(20)
        search_product_layout.addLayout(user_input_Hbox)
        #search_product_layout.addWidget(self.shop_by_department_combobox)
        #search_product_layout.addWidget(self.search_result_display)
        search_product_layout.addWidget(self.product_list_widget)
        search_product_layout.addWidget(self.display_tilemap_btn)
        search_product_layout.addWidget(self.main_menu_btn)
        search_product_layout.setGeometry(QtCore.QRect(140, 20, 461, 491))



        #initalizing the tilemap view
        #self.tilemap_page = TileMap()

        # Add pages (qwidgets) to the stacked widget----------- stacking widgets
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.search_product_page)
        # Connect signal for stacked widget's current widget change
        self.stacked_widget.currentChanged.connect(self.adjustParentSize)

        # Layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        

    def show_mainMenu_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_addItem_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def department_selected(self, dept):
        current_dept = dept

    
    #adding to our list & displaying to user
    def add_product_to_list(self):
        #get the str of product & save
        str = self.user_input_line.text()
        if str:
            product = myProductManager.get_product(str.lower())
            if  product is not None:
                if str.lower() not in product_list:
                    product_list.append(product)
                    #show in the list widget display
                    item = QListWidgetItem(product['Description'])
                    self.product_list_widget.addItem(item)
                    self.user_input_line.clear() #clear
                    #check
                    #print(product_list)
                else:
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle(" ")
                    dlg.setText("Product Already Added")
                    button = dlg.exec()

                    if button == QMessageBox.StandardButton.Ok:
                        print("ok")
            #elif(current_dept is not None):
                #product_by_dept_list = myProductManager.get_product_by_deptartment(current_dept)
                #for product in product_by_dept_list:
                    #self.shop_by_department_combobox.addItems(product)
            else:
                dlg = QMessageBox(self)
                dlg.setWindowTitle(" ")
                dlg.setText("Product Not Found")
                button = dlg.exec()

                if button == QMessageBox.StandardButton.Ok:
                    print("ok")
                
    
    def show_tilemap_page(self):
        
        self.tilemap_page = QWidget()
        tile_view_Hbox = QVBoxLayout(self.tilemap_page)
        main_menu_btn = QPushButton('Main Menu')
        main_menu_btn.clicked.connect(self.show_mainMenu_page)
        tile_view_Hbox.addWidget(main_menu_btn)

        view = TileMapView()
        myProductManager.populateShelves(view)

        # Pathfinding
        pathfinder = Pathfinder(view.tilemaps_widget)
        
        # making list of nodes based on product list
        for product in product_list:
            description = product['Description']
            item = myProductManager.get_product(description)
            pathfinder.add_node(item['Location'])

        path = pathfinder.find_path()
        view.tilemaps_widget.add_path(path)
        tile_view_Hbox.addWidget(view.tilemaps_widget)
        self.stacked_widget.addWidget(self.tilemap_page)
        self.stacked_widget.setCurrentIndex(2)
    
    def adjustParentSize(self, index):
        current_widget = self.stacked_widget.widget(index)
        if current_widget:
            self.resize(current_widget.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())