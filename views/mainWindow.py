import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, 
                             QListWidgetItem, QStackedWidget, QLineEdit, QListWidget, QHBoxLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackedWidget Demo')
        
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        #(1st page) Create pages (widgets) to add to the stacked widget
        self.page1 = QWidget()
        # Add labels to each page
        label1 = QLabel('italian sandwich')
        layout1 = QVBoxLayout(self.page1)
        layout1.addWidget(label1)

        #second page (widget)
        self.page2 = QWidget()
        #add label
        label2 = QLabel('taco')
        # line field for user input
        self.user_input_line = QLineEdit()
        self.user_input_line.setMaxLength(10)
        self.user_input_line.setPlaceholderText("Search product")

        #btn to submit str product
        self.submit_btn = QPushButton('Submit')
        self.submit_btn.clicked.connect(self.add_product_to_list)

        #horizontal layout for user input str function
        user_input_Hbox = QHBoxLayout()
        user_input_Hbox.addWidget(self.user_input_line)
        user_input_Hbox.addWidget(self.submit_btn)

        #list to store products
        self.product_list = []

        #list of input data
        self.product_list_widget = QListWidget()
        #self.product_list_widget.addItems(["One", "Two", "Three"])

        layout2 = QVBoxLayout(self.page2)
        layout2.addWidget(label2)
        layout2.addLayout(user_input_Hbox)
        layout2.addWidget(self.product_list_widget)

        # Add pages (qwidgets) to the stacked widget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Create buttons to switch between pages
        self.button_page1 = QPushButton('first page')
        self.button_page1.clicked.connect(self.show_page1)
        self.button_page2 = QPushButton('second page')
        self.button_page2.clicked.connect(self.show_page2)

        # Layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        layout.addWidget(self.button_page1)
        layout.addWidget(self.button_page2)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)
    
    #adding to our list & displaying to user
    def add_product_to_list(self):
        #get the str of product & save
        str = self.user_input_line.text()
        if str:
            self.product_list.append(str)
            #show in the list widget display
            item = QListWidgetItem(str)
            self.product_list_widget.addItem(item)
            self.user_input_line.clear() #clear
            #check
            #print(self.product_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
