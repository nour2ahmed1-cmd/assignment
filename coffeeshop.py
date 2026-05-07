#this is question 1 of the coffee shop problem
# prices
coffee_price = 25
cake_price = 40
water_price = 10

# quantities
coffee_quantity = 2
cake_quantity = 1
water_quantity = 3

# total bill
total_bill = (coffee_price * coffee_quantity) + (cake_price * cake_quantity) + (water_price * water_quantity)

print("Total bill: ", total_bill)
print("is the total bill greater than 100? ", total_bill > 100)
print ("is total bill equals 120?", total_bill == 120)

coffee_price += 5 # increase coffee price by 5 using reassignment operator
print("New total bill after price increase: ", (coffee_price * coffee_quantity) + (cake_price * cake_quantity) + (water_price * water_quantity))

#this is question 2 of the coffee shop problem
#Points
Points = 40 # initial points before the purchase
Points += 20 # earned 20 points from the purchase
Points -= 10 # redeemed 10 points for a discount
Points *= 2 # double the points for a special event 
# Final points
print("Final points: ", Points)

is_vip = Points >= 100
print("Is the customer a VIP? ", is_vip)

has_free_delivery = is_vip or total_bill > 150
print("Does the customer have free delivery? ", has_free_delivery)

#this is question 3 priority traps part A
result = 10 + 5 * 2 #multiplication perfoms before addition, so this will be 10 + (5*2) = 10 + 10 = 20
print(result) 

result = (10 + 5) * 2 #parentheses change the order of operations, so this will be (10 + 5) * 2 = 15 * 2 = 30
print(result) 

#this is question 3 priority traps part B
print(True or False and False) #and has higher precedence than or, so this will be evaluated as True or (False and False) = True or False = True
print((True or False) and False) #parentheses change the order of operations, so this will be (True or False) and False = True and False = False

#part c real life trap
total_bill = 120 
points = 20 
premium_member = True 
print(total_bill > 150 and points > 50 or premium_member) # and has higher precedence than or, so this will be evaluated as (total_bill > 150 and points > 50) or premium_member = (False and False) or True = False or True = True
print(total_bill > 150 and (points > 50 or premium_member)) # parentheses change the order of operations, so this will be total_bill > 150 and (points > 50 or premium_member) = False and (False or True) = False and True = False