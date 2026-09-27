import sqlite3

DATABASE_PATH = "database/canteen.db"


def add_sample_menu():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    menu_items = [
        ("Idli Sambar", "Breakfast", 40),
        ("Dosa", "Breakfast", 50),
        ("Veg Fried Rice", "Lunch", 80),
        ("Veg Biryani", "Lunch", 90),
        ("Chapati Curry", "Lunch", 70),
        ("Rice Sambar", "Lunch", 60),
        ("Tea", "Beverage", 15),
        ("Coffee", "Beverage", 20),
        ("Lemon Juice", "Beverage", 30),
    ]

    cursor.executemany(
        """
        INSERT INTO menu_items (name, category, price)
        VALUES (?, ?, ?)
        """,
        menu_items
    )

    connection.commit()
    connection.close()

    print("Sample menu added successfully!")


if __name__ == "__main__":
    add_sample_menu()