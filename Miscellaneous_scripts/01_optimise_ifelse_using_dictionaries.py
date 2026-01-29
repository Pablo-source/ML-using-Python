# Aim: Using get() method with dictionaries
#      It allows you to define a default method

food_item = input("Enter food item name:")

food_items_dict = { "burger": 9.00, 
                   "pizza": 7.35, 
                   "juice":2.15, 
                   "tofu":9.00}

# The get() method returns the value of an item with the specified key
# You can also specify a default value to return if the key is not found.

def getPrice(food_item):
    return food_items_dict.get(food_item, "item not found")

print(getPrice(food_item))

