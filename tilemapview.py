from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QStackedWidget
from tilemap import TileMap

#25x25 tile map
def custom_store_gen(tilemap: TileMap):
    #x = 1
    #y = 1
    #tilemap.place_object(1, 1, 'shelf_white_single_1')

    #Registers
    tilemap.place_dec(2,2, 'counter_corner_green')
    tilemap.place_dec(2,2, 'cash_register_green')
    tilemap.place_dec(3,1, 'counter_side_green')

    tilemap.place_dec(5,2, 'counter_corner_green')
    tilemap.place_dec(5,2, 'cash_register_green')
    tilemap.place_dec(6,1, 'counter_side_green')

    tilemap.place_dec(8,2, 'counter_corner_green')
    tilemap.place_dec(8,2, 'cash_register_green')
    tilemap.place_dec(9,1, 'counter_side_green')

    tilemap.place_dec(11,2, 'counter_corner_green')
    tilemap.place_dec(11,2, 'cash_register_green')
    tilemap.place_dec(12,1, 'counter_side_green')

    tilemap.place_dec(14,2, 'counter_corner_green')
    tilemap.place_dec(14,2, 'cash_register_green')
    tilemap.place_dec(15,1, 'counter_side_green')

    tilemap.place_dec(17,2, 'counter_corner_green')
    tilemap.place_dec(17,2, 'cash_register_green')
    tilemap.place_dec(18,1, 'counter_side_green')

    tilemap.place_dec(20,2, 'counter_corner_green')
    tilemap.place_dec(20,2, 'cash_register_green')
    tilemap.place_dec(21,1, 'counter_side_green')

    #Isles
    # for y in range(tilemap.height // 4 - 1):
    #     for x in range(tilemap.width // 2 - 2):
    #         tilemap.place_object(2 * x + 2, y * 4 + 6, 'shelf_white_double')
    tilemap.place_object(2, 6, 'shelf_white_double')
    tilemap.place_object(4, 6, 'shelf_white_double')
    tilemap.place_object(6, 6, 'shelf_white_double')
    tilemap.place_object(8, 6, 'shelf_white_double')

    tilemap.place_object(14, 6, 'shelf_white_double')
    tilemap.place_object(16, 6, 'shelf_white_double')
    tilemap.place_object(18, 6, 'shelf_white_double')
    tilemap.place_object(20, 6, 'shelf_white_double')

    #################################################

    tilemap.place_object(8, 10, 'shelf_white_double')
    tilemap.place_object(10, 10, 'shelf_white_double')
    tilemap.place_object(12, 10, 'shelf_white_double')
    tilemap.place_object(14, 10, 'shelf_white_double')

    ##################################################

    tilemap.place_object(2, 14, 'shelf_white_double')
    tilemap.place_object(4, 14, 'shelf_white_double')
    tilemap.place_object(6, 14, 'shelf_white_double')
    tilemap.place_object(8, 14, 'shelf_white_double')

    tilemap.place_object(14, 14, 'shelf_white_double')
    tilemap.place_object(16, 14, 'shelf_white_double')
    tilemap.place_object(18, 14, 'shelf_white_double')
    tilemap.place_object(20, 14, 'shelf_white_double')
    



    #sides
    tilemap.place_dec(5,18, 'shelf_white_double_side')
    tilemap.place_dec(7,18, 'shelf_white_double_side')
    tilemap.place_dec(9,18, 'shelf_white_double_side')
    tilemap.place_dec(11,18, 'shelf_white_double_side')
    tilemap.place_dec(13,18, 'shelf_white_double_side')
    tilemap.place_dec(15,18, 'shelf_white_double_side')
    tilemap.place_dec(17,18, 'shelf_white_double_side')

    tilemap.place_dec(2,10, 'shelf_white_double_side')
    tilemap.place_dec(4,10, 'shelf_white_double_side')
    tilemap.place_dec(6,10, 'shelf_white_double_side')

    tilemap.place_dec(17,10, 'shelf_white_double_side')
    tilemap.place_dec(19,10, 'shelf_white_double_side')
    tilemap.place_dec(21,10, 'shelf_white_double_side')

    

    
    # tilemap.place_dec(5, 2, 'cash_register_green')
    # tilemap.place_dec(8, 2, 'cash_register_green')
    # tilemap.place_dec(11, 2, 'cash_register_green')
    # tilemap.place_dec(14, 2, 'cash_register_green')
    # tilemap.place_dec(17, 2, 'cash_register_green')
    # tilemap.place_dec(20, 2, 'cash_register_green')

    #tilemap.place_dec(2,3, 'counter_side_green')
    #tilemap.place_dec(2,2, 'counter_side_green')
    #tilemap.place_dec(2,1, 'counter_side_green')
 
    #shelf_white_single_0

def default_store_gen(tilemap: TileMap):
    for y in range(tilemap.height // 4 - 1):
        for x in range(tilemap.width // 2 - 2):
            tilemap.place_object(2 * x + 2, y * 4 + 5, 'shelf_white_double')
    tilemap.place_dec(2, 1, 'cash_register')

class TileMapView(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 700)        
        self.tilemaps_widget = TileMap(25, 25)
        custom_store_gen(self.tilemaps_widget)

        # Add widget to layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tilemaps_widget)
        self.setLayout(main_layout)
    
    def getShelves(self):
        return self.tilemaps_widget.get_objects()

