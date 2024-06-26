from api import API


class Product:
    def __init__(self,
                 upc,
                 desc,
                 price,
                 department,
                 store_discount=0,
                 loyalty_discount=0,
                 digital_coupon=0):
        self.upc = upc
        self.desc = desc
        self.price = price
        self.department = department
        self.store_discount = store_discount
        self.loyalty_discount = loyalty_discount
        self.digital_coupon = digital_coupon
        self.tile = None # In storage
        
        
class ProductManager:
    def __init__(self):
        #print("check...")
        self.products = [] 

    def initializeProducts(self):
        #print("starting...")

        #get list of items
        myAPI = API()
        items = myAPI.getItemDetails()
        #print("got the API STUFF")
        self.products = items
        #sort list by departments
        self.products = sorted(self.products, key=lambda x: x["Department"])

        
    def printProductsToText(self):
        # Open a file in write mode ('w')
        with open('output.txt', 'w') as file:
            # Iterate over each element in the list
            for item in self.products:
                # Write each element followed by a newline character to the file
                file.write(str(item) + '\n')

    # Method that sets tuples for each product representing location
    # 2 products per shelf, iterate until we run out of shelves or the list ends
    def populateShelves(self, storeTileMap):
        print("about to populate the shelves")
        shelves = storeTileMap.getShelves()

        for count, product in enumerate(self.products):
            shelf = shelves[count % len(shelves)]
            # Adding access point offset to the shelf position so item is accessed from the front
            access_point_offset = 1
            shelve_pos = list(shelf[:2])
            shelve_pos[1] += access_point_offset
            product['Location'] = shelve_pos
        self.printProductsToText()
        
        
    def add_product(self, product):
        self.products.append(product)
        
        
    def get_product(self, description):
        for product in self.products:
            if product['Description'] == description:
                return product
        return None
    
    def get_department(self):
        department_list = []
        for product in self.products:
            if product['Department'] not in department_list:
                department_list.append(product)
        return department_list


    def get_product_by_deptartment(self, department):
        product_by_dept_list = []
        for product in self.products:
            if product['department'] == department:
                product_by_dept_list.append(product)
        return product_by_dept_list
    
    def remove_product(self, upc):
        for product in self.products:
            if product.upc == upc:
                self.products.remove(product)
                return True
        return False
        
        
    def update_product(self, upc, product):
        for i, product in enumerate(self.products):
            if product.upc == upc:
                self.products[i] = product
                return True
        return False
