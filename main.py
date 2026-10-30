from time import sleep
from subprocess import run

from inventory import (
    add_product,
    display_inventory,
    search_product,
    update_stock,
    calculate_inventory_value,
    save_inventory,
    load_inventory
)

def main():
    inventory = load_inventory()

    while True:
        run(["clear"], check=False)
        # Display menu
        print(f"\n{'='*10} INVENTORY MANAGER {'='*10}\n")
        print("1. Display inventory")
        print("2. Add product")
        print("3. Search product by ID")
        print("4. Update stock")
        print("5. Calculate inventory value")
        print("6. Save inventory")
        print("7. Exit")

        # Get user's choice
        user_input = input(">>> ").strip().lower()
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Please enter a number.")
            sleep(2)
            continue

        # Handle user's choice
        if user_choice == 1:
            display_inventory(inventory)
            input("\nPress enter to get back to the menu.")
            continue
        elif user_choice == 2:
            inventory = add_product(inventory)
            input("Press enter to get back to the menu.")
            continue
        elif user_choice == 3:
            search_result = search_product(inventory)
            if search_result:
                display_inventory(search_result)
            print()
            input("Press enter to get back to the menu.")
            continue
        elif user_choice == 4:
            inventory = update_stock(inventory)
            input("Press enter to get back to the menu.")
            continue
        elif user_choice == 5:
            print(f"Total inventory value = {calculate_inventory_value(inventory)}")
            input("Press enter to get back to the menu.")
            continue
        elif user_choice == 6:
            try:
                save_inventory(inventory)
                print("Inventory saved successfully in inventory.json file.\n")
            except (OSError, TypeError, ValueError) as error:
                print(f"Failed to save inventory: {error}")
            input("Press enter to get back to the menu.")
            continue

        # Exit condition
        elif user_choice == 7:
            while True:
                confirm_exit = input(
                    "Save updates, discard them, or go back to the menu?\n"
                    "Type s to save, d to discard, or b to go back.\n>>> "
                ).strip().lower()

                if confirm_exit == "s":
                    try:
                        save_inventory(inventory)
                    except (OSError, TypeError, ValueError) as error:
                        print(f"Failed to save inventory: {error}")
                        continue
                    break
                elif confirm_exit in ("d", "b"):
                    break
                else:
                    print("Please enter s, d, or b.")

            if confirm_exit == "b":
                continue
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")
            sleep(2)


if __name__ == "__main__":
    main()