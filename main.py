

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

def product_id_exists(id: str, inventory: dict) -> bool:
    """To check whether the ID already exist or not."""
    return id in inventory

def add_product(inventory: dict):
    """Adding a new product through terminal input."""
    inv_temp = inventory.copy()
    product_id = input("Enter product ID: ")
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

