import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackedWidget Demo')
        
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Create pages (widgets) to add to the stacked widget
        self.page1 = QWidget()
        self.page2 = QWidget()
        
        # Add labels to each page
        label1 = QLabel('italian sandwich')
        label2 = QLabel('taco')
        layout1 = QVBoxLayout(self.page1)
        layout2 = QVBoxLayout(self.page2)
        layout1.addWidget(label1)
        layout2.addWidget(label2)

        # Add pages to the stacked widget
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
