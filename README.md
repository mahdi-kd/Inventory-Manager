# Inventory Manager

A simple command-line inventory management application built with Python. This project was created as a practical exercise to improve my Python programming skills.

## Features

- Add new products to the inventory
- Display all products
- Search for products by ID
- Update product stock
- Calculate the total inventory value
- Save inventory data to a JSON file
- Load inventory data from a JSON file
- Validate inventory data and handle errors
- Interactive command-line menu for accessing different operations
- Choose whether to save changes, discard them, or return to the menu when exiting

## Requirements

- Python 3

No external libraries are required. The project uses Python's standard library.

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Run the following command:

```bash
python main.py
```

## Usage

After running the program, an interactive menu will appear with the following options:

1. Display inventory
2. Add product
3. Search product by ID
4. Update stock
5. Calculate inventory value
6. Save inventory
7. Exit

When exiting, you can choose to save your changes, discard them, or return to the menu.

## Project Structure

```text
inventory-manager/
├── main.py
├── inventory.py
├── inventory.example.json
├── .gitignore
└── README.md
```

- `main.py`: Handles the main program flow and user interaction.
- `inventory.py`: Contains the inventory management functions.
- `.gitignore`: Specifies files and directories Git should ignore.
- `README.md`: Project documentation.

## What I Learned

Through this project, I practiced:

- Working with dictionaries and nested data structures
- Writing and organizing functions
- Modularizing code using Python modules
- Handling user input and validating data
- Using exceptions for error handling
- Working with JSON for data persistence
- Building an interactive command-line application
- Using Git for version control