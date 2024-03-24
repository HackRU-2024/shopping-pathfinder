import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
                             QListWidgetItem, QStackedWidget, QLineEdit, QListWidget, QHBoxLayout)
from PyQt6 import QtCore
#from tilemap import TileMap
#list to store products
product_list = []

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
        #self.display_tilemap_btn.clicked.connect(self.show_tilemap_page)

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
        self.stacked_widget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
