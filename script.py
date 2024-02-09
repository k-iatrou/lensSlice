# Creating lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# counting amount of $2 slices in the list
num_two_dollar_slices = prices.count(2)

# getting length of the toppings
num_pizzas = len(toppings)

# printing out how many pizzas we offer
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
