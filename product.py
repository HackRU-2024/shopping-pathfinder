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

        shelfCapacity = 0
        i = 0
        for item in self.products:
            if(shelfCapacity != 2 and i != len(shelves)):
                # Adding access point offset to the shelf position so item is accessed from the front
                access_point_offset = 1
                shelve_pos = list(shelves[i][:2])
                shelve_pos[1] += access_point_offset
                item['Location'] = shelve_pos
                shelfCapacity += 1
                if(shelfCapacity ==2):
                    shelfCapacity = 0
                    i+=1
            elif(i == len(shelves)):
                print("ran out of shelves...")
                break
            #else:
                #shelfCapacity = 0
                #i += 1

        self.printProductsToText()

        #print(shelves)
        #return NULL 

    def add_product(self, product):
        self.products.append(product)
        
        
    def get_product(self, description):
        for product in self.products:
            if product['Description'] == description:
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
