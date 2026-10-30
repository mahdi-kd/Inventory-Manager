from copy import deepcopy
import json

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
                if p_price <= 0:
                    print("Price must be positive.")
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

def search_product_id(inventory: dict, product_id: str) -> dict:
    """Search the inventory dictionary by product ID."""

    product_id = product_id.strip().lower()
    if product_id in inventory:
        return inventory[product_id]
    return None

def search_product(inventory: dict) -> dict:
    product_id = input("Enter a Product ID: ").strip().lower()
    result = search_product_id(inventory, product_id)
    if result:
        return {product_id: result}
    else:
        print("No matching product ID found.")
        return None

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

def calculate_inventory_value(inventory: dict) -> int:
    """Calculate the total value of all products in inventory. """
    total_value = 0
    for p_info in inventory.values():
        total_value += p_info['price'] * p_info['quantity']
    return total_value

def save_inventory(inventory: dict) -> None:
    with open("inventory.json", 'w') as file:
        json.dump(inventory, file, indent=4)

def validate_inventory(inventory: dict) -> bool:
    if not isinstance(inventory, dict):
        return False
    products = inventory.values()
    try:
        if all(
                isinstance(key, str) and isinstance(value, dict) 
                for key, value in inventory.items()
            ) and all(  #Check datatype of product info
                isinstance(product['name'], str) and
                isinstance(product['price'], int) and
                not isinstance(product['price'], bool) and
                isinstance(product['quantity'], int) and
                not isinstance(product['quantity'], bool)
                for product in products
            ) and all(  #Check valid value for product info
                product['price'] > 0 and
                product['quantity'] >= 0
                for product in products
            ):
                return True
    except KeyError:
        return False
    return False

def load_inventory() -> dict:
    try:
        with open("inventory.json", 'r') as file:
            inv_temp = json.load(file)
    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.")
        return {}
    except json.JSONDecodeError:
        print("inventory.json is corrupted. Starting with an empty inventory.")
        return {}
    if validate_inventory(inv_temp):
        return inv_temp

    print("inventory.json is invalid. Starting with an empty inventory.")
    return {}

