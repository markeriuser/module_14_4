import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

def populate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    products = [
        ("Продукт 1", "Описание продукта 1", 100),
        ("Продукт 2", "Описание продукта 2", 200),
        ("Продукт 3", "Описание продукта 3", 300),
        ("Продукт 4", "Описание продукта 4", 400),
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()

initiate_db()
populate_db()
