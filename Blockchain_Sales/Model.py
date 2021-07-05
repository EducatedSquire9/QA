class Invoice:
    def __init__(self, product, quantity, price, date_time):
        self._id = 0
        self._product = product
        self._quantity = quantity
        self._price = price
        self._date_time = date_time

    def get_id(self): return self._id

    def get_product(self): return self._product

    def get_quantity(self): return self._quantity

    def get_price(self): return self._price

    def get_date_time(self): return self._date_time

    def __str__(self):
        return '{ "product" : "' + str(self._product) + '", "quantity" : ' + str(
            self._quantity) + ' , "price" : ' + str(
            self._price) + '}'


# x = Invoice('dsf', 3, 33)
#
# print(x)