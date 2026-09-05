def ShoppingCart(cart):
    cart.append("orange")

cart = ["apple", "jam", "banana"]

print("Before calling function:", cart)

ShoppingCart(cart)

print("After calling function:", cart)