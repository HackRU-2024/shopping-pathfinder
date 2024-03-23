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
        print("check...")
        self.products = [] 

    def initializeProducts(self):
        print("starting...")

        #get list of items
        myAPI = API()
        items = myAPI.getItemDetails()
        print("got the API STUFF")
        self.products = items

        # Open a file in write mode ('w')
        with open('output.txt', 'w') as file:
            # Iterate over each element in the list
            for item in self.products:
                # Write each element followed by a newline character to the file
                file.write(str(item) + '\n')

        
    def add_product(self, product):
        self.products.append(product)
        
    def get_product(self, upc):
        for product in self.products:
            if product.upc == upc:
                return product
        return None
    
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