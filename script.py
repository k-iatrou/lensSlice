# Creating lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# counting amount of $2 slices in the list
num_two_dollar_slices = prices.count(2)

# getting length of the toppings
num_pizzas = len(toppings)

# printing out how many pizzas we offer
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# 2D list for prices and toppings and output to console
pizza_and_price = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

print(pizza_and_price)

# sorted the pizza and price list ascending
pizza_and_price = sorted(pizza_and_price)

# cheapest pizza
cheapest_pizza = pizza_and_price[0]

# priciest pizza
priciest_pizza = pizza_and_price[-1]

# removing anchovies from list
pizza_and_price.pop()

# adding new topping
pizza_and_price = pizza_and_price + [2.5, "peppers"]

#slicing out the 3 cheapest slices from the list
three_cheapest = pizza_and_price[:3]

# printing 3 cheapest slices
print(three_cheapest)