

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

def id_check(id: str, inventory: dict) -> bool:
    """To check whether the ID already exist or not."""
    return id in inventory.keys()

def add_product(inventory: dict):
    p_id = input("Enter product ID: ")
    if id_check(p_id, inventory):
        p_name = input("Enter product name: ")
        while True:
            try:
                p_price = int(input("Enter price: "))
                break
            except ValueError:
                print("Please enter a valid number. Avoid using special characters.")
        while True:
            try:
                p_quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Please enter a valid number. Avoid using special characters.")
    else:
        print(f"The product ID {p_id} already exists.")
    inventory[p_id] = {
        "name" : p_name,
        "price" : p_price,
        "quantity" : p_quantity
    }
