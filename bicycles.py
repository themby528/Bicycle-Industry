#Create Bicycle class
class bicycle(object):
    def __init__(self,model,weight,cost):
        self.model = model
        self.weight = weight
        self.cost = cost

#Create Bike Shop class
class bike_shop(object):
    def __init__(self,name,inventory_name,inventory_number):
        self.name = name
        self.inventory_name = inventory_name
        self.inventory_number = inventory_number
        
    def price(self, cost):
        return float(cost) * 1.2
    
    def profit(self, price, cost):
        return price - cost
        
#Create Customer class
class customer(object):
    def __init__(self,name,funds, own):
        self.name = name
        self.funds = funds
        self.own = own
        
