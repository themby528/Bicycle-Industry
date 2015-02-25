#Import the classes from bicycles
from bicycles import *

#Create 6 bicycle models 
bike1 = bicycle("Tour",100, 200)
bike2 = bicycle("France",60, 500)
bike3 = bicycle("Yellow",55, 800)
bike4 = bicycle("Frank",150, 100)
bike5 = bicycle("Andy",75,350)
bike6 = bicycle("Schleck",200, 25)

#Create a bike shop
TheBikeShop = bike_shop("The Bike Shop",[bike1, bike2, bike3, bike4, bike5, bike6],[5,7,11,3,8,9])

#Create 3 customers
Cust1 = customer("Larry",100, "none")
Cust2 = customer("Moe",200, "none")
Cust3 = customer("Curly",1000, "none")

#store the customers in a list to loop over them
customers = [Cust1, Cust2, Cust3]

#Print all the customers and which bicycle models fall within their budget
print "Customers and potential models-----"
for n in customers:
    print "Customer: " + n.name
    for i in TheBikeShop.inventory_name:
        if TheBikeShop.price(i.cost) <= n.funds:
            print i.model

#Print the current inventory of the bike shop
print "Current Inventory ------"
for i in range(0,6):
    print "Model: %s" %TheBikeShop.inventory_name[i].model
    print "In Stock: %s" %TheBikeShop.inventory_number[i]
    
#Pick a model for each person to buy
Cust1.own = "Schleck"
Cust2.own = "Frank"
Cust3.own = "Yellow"
  
#Print the customer, model purchase and remaining funds
print "Purchases -----"
for n in customers:
    print "Customer: " + n.name
    print "Model purchased: " + n.own
    for i in TheBikeShop.inventory_name:
        if i.model == n.own:
            print "Cost: %s" %TheBikeShop.price(i.cost)
            print "Remaining Funds: %s" %(n.funds - TheBikeShop.price(i.cost))

#Print updates to the Bike Shope inventory
print "Updates to Inventory -----"
profit = 0
for i in range(0,6):
    print "Model: " + TheBikeShop.inventory_name[i].model
    for n in customers:
        if n.own == TheBikeShop.inventory_name[i].model:
            TheBikeShop.inventory_number[i] -= 1
            profit = profit +  TheBikeShop.profit(TheBikeShop.price(TheBikeShop.inventory_name[i].cost),TheBikeShop.inventory_name[i].cost)
    print "In Stock: %s" %TheBikeShop.inventory_number[i]
print "Total profit: %s" %profit
        