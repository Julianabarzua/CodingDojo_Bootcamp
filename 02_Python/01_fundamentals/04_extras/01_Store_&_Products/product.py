class product:
    prod_id=0

    def __init__(self, name, price, cat):
        self.name = name
        self.price = price
        self.category = cat
        self.id = product.prod_id
        product.prod_id +=1

    def update_price(self, rate, toohigh):
        change = self.price*rate
        if toohigh :
            self.price +=change
        else:
            self.price -=change

    def print_info(self):
        print(f'{self.id} - {self.name} - ${self.price} - {self.category}')