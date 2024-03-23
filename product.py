class Product:
    def __init__(self,
                 upc,
                 desc,
                 price,
                 store_discount=0,
                 loyalty_discount=0,
                 digital_coupon=0):
        self.upc = upc
        self.desc = desc
        self.price = price
        self.store_discount = store_discount
        self.loyalty_discount = loyalty_discount
        self.digital_coupon = digital_coupon