

inventory = {
    "p001" : {
        "name" : "Headphone",
        "price" : 150,
        "quantity" : 24
    },
    "p002" : {
        "name" : "Printer",
        "price" : 300,
        "quantity" : 5
    },
    "p003" : {
        "name" : "Mobile Phone",
        "price" : 250,
        "quantity" : 15
    }
}

def product_id_exists(product_id: str, inventory: dict) -> bool:
    """To check whether the ID already exist or not."""
    return product_id in inventory

def add_product(inventory: dict):
    """Adding a new product through terminal input."""
    inv_temp = inventory.copy()
    product_id = input("Enter product ID: ").strip().lower()
    if not product_id_exists(product_id, inventory):
        p_name = input("Enter product name: ")
        while True:
            try:
                p_price = int(input("Enter price: "))
                if p_price < 0:
                    print("Price can't be negetive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid non-negative integer number. Avoid using special characters.")
        while True:
            try:
                p_quantity = int(input("Enter quantity: "))
                if p_quantity < 0:
                    print("Quantitiy can't be negetive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid non-negative integer number. Avoid using special characters.")
    else:
        print(f"The product ID {product_id} already exists.")
        return inv_temp
    inv_temp[product_id] = {
        "name" : p_name,
        "price" : p_price,
        "quantity" : p_quantity
    }
    return inv_temp

def display_inventory(inventory: dict):
    """Display the inventory storage."""

    if not inventory:
        print("Inventory is empty.")
        return
    print(f"\n{'ID' :<10}  | {'NAME':<20}| {'PRICE' :<15}| {'QUANTITY' :<15} \n{'-'*67}")
    for product, p_info in inventory.items():
        print(f"| {product :<10}| {p_info['name'] :<20}| {p_info['price'] :<15}| {p_info['quantity'] :<15}")

def search_product_id(inventory :dict, product_id :str) -> dict:
    """Search the inventory dictionary by product ID."""

    product_id = product_id.strip().lower()
    if product_id in inventory:
        return inventory[product_id]
    return None

def search_product(inventory :dict) -> dict:
    product_id = input("Enter a Product ID: ").strip().lower()
    result = search_product_id(inventory, product_id)
    if result:
        return {product_id: result}
    else:
        print("No matching product ID found.")
        return None

from copy import deepcopy
def update_stock(inventory: dict):
    """Update quantity of one product."""
    inv_temp = deepcopy(inventory)
    product_id = input("Enter a Product ID: ").strip().lower()
    if product_id_exists(product_id, inventory):    #Valid product ID
        item = search_product_id(inventory, product_id)
        print(f"Current quantity for {item['name']}: {item['quantity']}")
        while True:
            user_input = input(f"Enter 'a' for add, 'r' to remove a certain number and a non-negetive integer to set the quantity: \n").strip().lower()
            if user_input == 'a':    #Adding stock
                try:
                    add_value = int(input("How much to add: "))
                    if add_value < 0:
                        print("Amount cannot be negative.")
                        continue
                    inv_temp[product_id]['quantity'] += add_value
                    break
                except ValueError:
                    print("Invalid number. Please try again.")
            elif user_input == 'r':  #Removing stock
                try:
                    remove_value = int(input("How much to remove: "))
                    if remove_value < 0:
                        print("Amount cannot be negative.")
                        continue

                    if remove_value > inv_temp[product_id]['quantity']:
                        print("Not enough stock.")
                        continue
                    inv_temp[product_id]['quantity'] -= remove_value
                    break
                except ValueError:
                    print("Invalid number. Please try again.")
            else:                    #Setting stock
                try:
                    quantity_value = int(user_input)
                    if quantity_value < 0:
                        print("Amount cannot be negative.")
                        continue
                    inv_temp[product_id]['quantity'] = quantity_value
                    break
                except ValueError:
                    print("Invalid number. Please try again.")

    else:   #Invalid product ID
        print(f"Product with product ID: {product_id} doesn't exist.")
        return inv_temp
    return inv_temp

