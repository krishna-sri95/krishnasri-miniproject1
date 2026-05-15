#PART A — SPOT THE BUG
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", ["bread"]))
print(add_item("eggs"))

# The default list 'cart=[]' is created only once.
# So the same list is reused in multiple function calls.
# Hence all names stay in the same list

# PART B — FIX THE BUG
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print("\nFixed Function Output")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# PART C — SHOPPING CART
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }
    cart["items"].append(item)
def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]
    total = total - (total * cart["discount"] / 100)
    return total
def update_price(price_tuple):
    try:
        price_tuple[1] = 60000
    except TypeError:
        print("\nTuples are immutable")
        
cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Krishna", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

add_to_cart(cart2, "Phone", 20000, 1)

print("\nCart 1")
print(cart1)

print("\nCart 2")
print(cart2)

print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))

price_data = ("Laptop", 50000)

update_price(price_data)

# DISCUSSION POINTS

# Why is discount=0 safe but cart=[] dangerous?
# discount=0 is safe because int is immutable.
# cart=[] is dangerous because list is mutable.

# What is the difference between rebinding and mutating?
# Rebinding = assigning a new object.
# Mutating = changing the existing object.

# Which of these are mutable? — list, tuple, dict, set, str, int
# list, dict, set are mutable and tuple, str, int are immutable.

# When you pass a list into a function and modify it, do changes reflect outside? Why?
# Yes, because lists are mutable.
