import sqlite3

DATABASE_PATH = "database/canteen.db"


def create_tables():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # 1. Menu items
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            available INTEGER DEFAULT 1
        )
    """)

    # 2. Orders
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_date TEXT NOT NULL,
            order_time TEXT NOT NULL,
            student_name TEXT,
            total_amount REAL NOT NULL,
            status TEXT DEFAULT 'Placed'
        )
    """)

    # 3. Order items
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            menu_item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
        )
    """)

    # 4. Food preparation
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS food_preparation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            preparation_date TEXT NOT NULL,
            menu_item_id INTEGER NOT NULL,
            quantity_prepared REAL NOT NULL,
            predicted_demand REAL,
            FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
        )
    """)

    # 5. Leftovers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leftovers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_date TEXT NOT NULL,
            menu_item_id INTEGER NOT NULL,
            quantity REAL NOT NULL,
            reason TEXT,
            action_taken TEXT,
            FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
        )
    """)

    # 6. Waste records
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS waste_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_date TEXT NOT NULL,
            food_item TEXT,
            waste_type TEXT NOT NULL,
            waste_source TEXT,
            quantity_kg REAL NOT NULL,
            reason TEXT,
            disposal_method TEXT,
            image_path TEXT
        )
    """)

    # 7. Student feedback
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feedback_date TEXT NOT NULL,
            menu_item_id INTEGER,
            rating INTEGER,
            comment TEXT,
            FOREIGN KEY (menu_item_id) REFERENCES menu_items(id)
        )
    """)

    # 8. Alerts
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_date TEXT NOT NULL,
            alert_type TEXT NOT NULL,
            message TEXT NOT NULL,
            severity TEXT DEFAULT 'Medium',
            resolved INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()

    print("All database tables created successfully!")


if __name__ == "__main__":
    create_tables()