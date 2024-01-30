class Coffee:
    
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self,'name') == False:
            if isinstance(name,str) and len(name)>=3:
                self._name = name 
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        list_of_customers = [order.customer for order in Order.all if order.coffee == self]
        set_of_customers = set(list_of_customers)
        unique_list_of_customers = list(set_of_customers)
        return unique_list_of_customers

    def num_orders(self):
        num_of_orders = 0
        for order in Order.all:
            if order.coffee == self:
                num_of_orders +=1

        return num_of_orders
    
    def average_price(self):
        total_price = 0
        total_coffee_orders=0
        for order in Order.all:
            if order.coffee == self:
                total_price+=order.price
                total_coffee_orders+=1

        if total_coffee_orders == 0:
            return total_coffee_orders

        return total_price/total_coffee_orders
        

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str) and (len(name)>=1 and len(name)<=15):
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        list_of_coffees = [order.coffee for order in Order.all if order.customer == self]
        set_of_coffees = set(list_of_coffees)
        unique_list_of_coffees = list(set_of_coffees)

        return unique_list_of_coffees
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee,price)
        return new_order
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        if hasattr(self,'price') == False:
            if isinstance(price, float) and (price>=1.0 and price <=10.0):
                self._price = price
