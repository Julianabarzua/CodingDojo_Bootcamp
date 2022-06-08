class store:

    def __init__(self, name):
        self.name = name
        self.prod_list = []

    def add_product(self, new_product):
            self.prod_list.append(new_product)

    def sell_product(self, id):
        # self.prod_list[id].print_info()
        self.prod_list.pop(id)

    def inflation(self, rate):
        for product in self.prod_list:
            product.update_price(rate, True)

    def sales(self, rate):
        for product in self.prod_list:
            product.update_price(rate, False)
    
    def print_prod(self):
        print('\nProducts in store:')
        for prod in self.prod_list:
            prod.print_info()